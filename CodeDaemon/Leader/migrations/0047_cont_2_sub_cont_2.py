# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20170724_1513'),
        ('home', '0015_problem_s_rate'),
        ('Leader', '0046_auto_20170730_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_time', models.DateTimeField(blank=True)),
                ('tot_score', models.IntegerField(default=0)),
                ('Divisible_Integer', models.IntegerField(default=0)),
                ('Lucifer_and_Subsequences', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'ordering': ['-tot_score', 'sub_time'],
            },
        ),
        migrations.CreateModel(
            name='Sub_cont_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('time', models.DateTimeField()),
                ('Lang', models.CharField(max_length=10)),
                ('pts', models.IntegerField(default=0)),
                ('res', models.CharField(max_length=100)),
                ('Problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problem')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
