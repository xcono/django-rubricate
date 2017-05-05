from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rubricate import attachments


@csrf_exempt
def attachment_add(request):

    code = 405
    response = {
        'status': 'false',
        'message': 'Method Not Allowed. Only method POST allowed.',
        'path': '',
        'filename': ''
    }

    if request.method == "POST":

        if request.FILES['file']:

            response['filename'] = request.FILES['file'].name

            try:
                code = 200
                response['path'] = attachments.attachment_upload(request.FILES['file'])
                response['message'] = 'Successfully uploaded.'
            except Exception as e:
                code = 204
                response['message'] = 'File save error. ' + str(e)
        else:
            code = 204
            response['message'] = 'Empty request. Cannot find a file attached to request.'

    return JsonResponse(status=code, data=response)
