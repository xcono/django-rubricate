import os
import uuid
import shutil
import tempfile
import logging
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def attachment_upload(file):
    """
    Move file to os temporary folder.
    :param file:
    :return: string
    """
    fs = FileSystemStorage(tempfile.gettempdir())
    filename = fs.save(tempfile.NamedTemporaryFile().name, file)
    return fs.path(filename)


def attachment_process(stream_data):

    for plugin in stream_data.get('plugins', []):
        if plugin.get('uploads'):
            for key, attachment in enumerate(plugin.get('uploads')):

                # move temporary file to permanent directory
                if attachment.get('temp'):
                    attachment_save(attachment)

                # remove attachment marked as "remove"
                if attachment.get('remove'):
                    attachment_remove(attachment)
                    plugin.get('uploads').remove(attachment)

    for attachment in stream_data.get('uploads_remove', []):
        attachment_remove(attachment)

    return stream_data


def attachment_save(attachment):

    # don't rise any exception if temporary file doesn't exist
    if not os.path.exists(attachment['path']):
        attachment['remove'] = True
        logging.error('Try to save stream attachment failed. File does not exist by path: ' + attachment['path'])

    ext = os.path.splitext(attachment['filename'])[1]
    filename = str(uuid.uuid4().hex) + ext
    folder = os.path.join(settings.MEDIA_ROOT, filename[0])

    # create the folder if it doesn't exist.
    if not os.path.exists(folder):
        try:
            os.mkdir(folder)
        except OSError as exc:
            logging.error(
                'Try to save stream attachment failed. '
                'Cannot create destination folder: {0} {1}'.format(folder, str(exc)))

    # save the uploaded file inside that folder.
    path = os.path.join(folder, filename)
    shutil.move(attachment['path'], path)

    attachment['path'] = path
    attachment['name'] = filename
    attachment['url'] = os.path.join(settings.MEDIA_URL, filename[0], filename)
    attachment['size'] = os.path.getsize(path)


def attachment_remove(attachment):
    try:
        os.remove(attachment['path'])
    except OSError:
        pass
