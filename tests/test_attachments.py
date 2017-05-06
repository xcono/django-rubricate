#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-rubricate
------------

Tests for `django-rubricate` models module.
"""
import json
import os
from django.test import TestCase


class TestRubricate(TestCase):

    def setUp(self):
        pass

    def test_upload(self):
        # Create an instance of a POST request.
        with open('tests/filemock.jpg', 'rb') as fp:
            # test request
            response = self.client.post('/uploads/add', {'name': 'filemock.jpg', 'file': fp})
            self.assertEqual(response.status_code, 200)
            # test response
            data = json.loads(response.content.decode("utf-8"))
            self.assertEqual(os.path.exists(data.get('path')), True)

    def tearDown(self):
        pass
