# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leader', '0003_delete_vvt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ajay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120)),
                ('sub_time', models.TimeField()),
                ('tot_score', models.IntegerField(default=0)),
                ('p_id_0', models.IntegerField(default=0)),
                ('p_id_1', models.IntegerField(default=0)),
                ('p_id_2', models.IntegerField(default=0)),
                ('p_id_3', models.IntegerField(default=0)),
                ('p_id_4', models.IntegerField(default=0)),
            ],
        ),
    ]
