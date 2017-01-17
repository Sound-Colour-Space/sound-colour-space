# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-04 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0031_auto_20161104_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggedobject',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='museums_tagged_objects', to='museum.Keyword'),
        ),
    ]