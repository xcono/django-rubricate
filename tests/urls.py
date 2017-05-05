# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from rubricate.urls import urlpatterns as rubricate_urls

urlpatterns = [
    url(r'^', include(rubricate_urls, namespace='rubricate')),
]
