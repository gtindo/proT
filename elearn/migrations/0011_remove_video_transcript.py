# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-10 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0010_video_transcript'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='transcript',
        ),
    ]
