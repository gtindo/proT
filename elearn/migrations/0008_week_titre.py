# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-31 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0007_cours_niveau'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='titre',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
