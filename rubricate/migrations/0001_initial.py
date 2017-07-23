# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-23 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RubricatePermissionsSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'permissions': (('upload_files', 'Allowed to upload files attached to rubrics'),),
            },
        ),
    ]