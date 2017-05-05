from django.conf.urls import url
from rubricate import views

urlpatterns = [
    url(r'^attachment/add$', views.attachment_add),
]
