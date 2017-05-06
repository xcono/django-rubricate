from django.conf.urls import url
from rubricate import views

urlpatterns = [
    url(r'^uploads/add$', views.attachment_add, name='rubricate__attachment_add'),
]
