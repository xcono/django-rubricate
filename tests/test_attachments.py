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
from django.contrib.auth.models import User, Permission


class TestRubricate(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='pass')
        permission = Permission.objects.get(codename='upload_rubricate_files')
        self.user.user_permissions.add(permission)
        self.user.save()

    def test_upload(self):

        logged = self.client.login(username='user', password='pass')
        self.assertEqual(logged, True)

        # Create an instance of a POST request.
        with open('tests/filemock.jpg', 'rb') as fp:
            # test request
            response = self.client.post('/uploads/add', {'name': 'filemock.jpg', 'file': fp})
            self.assertEqual(response.status_code, 200)
            # test response
            data = json.loads(response.content.decode("utf-8"))
            self.assertEqual(os.path.exists(data.get('path')), True)

    def test_permissions(self):

        # self.client.logout()

        # Create an instance of a POST request.
        with open('tests/filemock.jpg', 'rb') as fp:
            # test request
            response = self.client.post('/uploads/add', {'name': 'filemock.jpg', 'file': fp})
            self.assertEqual(response.status_code, 403)

    def tearDown(self):
        self.user.delete()
