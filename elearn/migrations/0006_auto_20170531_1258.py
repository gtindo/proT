# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-31 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0005_enseignant_domaine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearn.Categorie'),
        ),
    ]
