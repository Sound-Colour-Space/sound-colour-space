# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-04 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0029_auto_20161104_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='term',
        ),
    ]
