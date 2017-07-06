import os
import uuid
import shutil
import tempfile
import logging
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def save_temporary(file):
    """
    Move file to os temporary folder.
    :param file:
    :return: string
    """
    fs = FileSystemStorage(tempfile.gettempdir())
    filename = fs.save(tempfile.NamedTemporaryFile().name, file)
    return fs.path(filename)


def uploads_process(json_data):

    for plugin in json_data.get('plugins', []):
        if plugin.get('uploads'):
            for key, attachment in enumerate(plugin.get('uploads')):

                # move temporary file to permanent directory
                if attachment.get('temp'):
                    uploads_save(attachment)

                # remove attachment marked as "remove"
                if attachment.get('remove'):
                    uploads_remove(attachment)
                    plugin.get('uploads').remove(attachment)

    for attachment in json_data.get('uploads_remove', []):
        uploads_remove(attachment)

    return json_data


def uploads_save(attachment):

    # don't rise any exception if temporary file doesn't exist
    if not os.path.exists(attachment['path']):
        attachment['remove'] = True
        logging.error('Try to save stream attachment failed. File does not exist by path: ' + attachment['path'])

    ext = os.path.splitext(attachment['filename'])[1]
    filename = str(uuid.uuid4().hex) + ext
    folder = _uploads_folder(filename)

    # save the uploaded file inside that folder.
    path = os.path.join(folder, filename)
    shutil.move(attachment['path'], path)

    attachment['path'] = path
    attachment['name'] = filename
    attachment['url'] = uploads_url(filename)
    attachment['size'] = os.path.getsize(path)


def uploads_remove(attachment):
    try:
        os.remove(attachment['path'])
    except OSError:
        pass


def _uploads_folder(filename):

    rubricate_folder = os.path.join(settings.MEDIA_ROOT, 'rubricate')

    if not os.path.exists(rubricate_folder):
        try:
            os.mkdir(rubricate_folder)
        except OSError as exc:
            logging.error(
                'Cannot create rubricate files folder. '
                'Cannot create rubricate files folder: {0} {1}'.format(rubricate_folder, str(exc)))

    folder = os.path.join(rubricate_folder, filename[0])

    # create the folder if it doesn't exist.
    if not os.path.exists(folder):
        try:
            os.mkdir(folder)
        except OSError as exc:
            logging.error(
                'Try to save stream attachment failed. '
                'Cannot create destination folder: {0} {1}'.format(folder, str(exc)))

    return folder


def uploads_url(filename):
    return os.path.join(settings.MEDIA_URL, 'rubricate', filename[0], filename)
