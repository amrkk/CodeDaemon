# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compile_run', '0026_adminsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsettings',
            name='buff',
            field=models.IntegerField(default=51200),
        ),
    ]
