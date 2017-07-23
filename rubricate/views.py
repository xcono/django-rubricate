from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rubricate import uploads


@csrf_exempt
def attachment_add(request):

    if not (request.user and request.user.has_perm('rubricate.upload_rubricate_files')):
        return HttpResponse(status=403, content='Upload is not allowed. You have no permissions to upload files.')

    if not request.method == 'POST':
        return HttpResponse(status=405, content='Method Not Allowed. Only method POST allowed.')

    file = request.FILES.get('file', None)

    if not file:
        return HttpResponse(status=204, content='Empty request. Cannot find a file attached to request.')

    try:
        response = {}
        response['filename'] = file.name
        response['path'] = uploads.save_temporary(file)
        response['message'] = 'Successfully uploaded.'
        return JsonResponse(status=200, data=response)
    except Exception as e:
        return HttpResponse(status=204, content='File save error. ' + str(e))
