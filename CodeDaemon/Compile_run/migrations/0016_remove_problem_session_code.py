# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compile_run', '0015_auto_20170709_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='session_code',
        ),
    ]
