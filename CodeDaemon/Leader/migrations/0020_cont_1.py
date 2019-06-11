# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leader', '0019_auto_20170710_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_time', models.TimeField()),
                ('tot_score', models.IntegerField(default=0)),
                ('fus', models.IntegerField(default=0)),
                ('gandul', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leader.User')),
            ],
            options={
                'ordering': ['-tot_score', 'sub_time'],
            },
        ),
    ]
