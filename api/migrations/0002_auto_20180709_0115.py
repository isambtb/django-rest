# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-09 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
