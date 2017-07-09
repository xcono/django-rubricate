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
            for upload in plugin.get('uploads', []):

                # move temporary file to permanent directory
                if upload.get('temp'):
                    uploads_save(upload)

                # remove attachment marked as "remove"
                if upload.get('remove'):
                    uploads_remove(upload)
                    plugin.get('uploads').remove(upload)

    for upload in json_data.get('uploads_remove', []):
        uploads_remove(upload)
        json_data.get('uploads_remove').remove(upload)

    return json_data


def uploads_save(upload):

    # don't rise any exception if temporary file doesn't exist
    if not os.path.exists(upload['path']):
        upload['remove'] = True
        logging.error('Try to save stream attachment failed. File does not exist by path: ' + upload['path'])

    ext = os.path.splitext(upload['filename'])[1]
    filename = str(uuid.uuid4().hex) + ext
    folder = _uploads_folder(filename)

    # save the uploaded file inside that folder.
    path = os.path.join(folder, filename)
    shutil.move(upload['path'], path)

    upload.update({
        'path': path,
        'name': filename,
        'url': uploads_url(filename),
        'size': os.path.getsize(path),
        'temp': 0,
    })


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
        except OSError:
            logging.error('Cannot create rubricate files folder in %s', rubricate_folder)

    folder = os.path.join(rubricate_folder, filename[0])

    # create the folder if it doesn't exist.
    if not os.path.exists(folder):
        try:
            os.mkdir(folder)
        except OSError:
            logging.error(
                'Try to save stream attachment failed in %s', folder)

    return folder


def uploads_url(filename):
    return os.path.join(settings.MEDIA_URL, 'rubricate', filename[0], filename)
