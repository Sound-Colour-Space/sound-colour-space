# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0004_auto_20160412_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', django_extensions.db.fields.UUIDField(blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('url', models.URLField(verbose_name='url')),
            ],
            options={
                'ordering': ('-created',),
                'db_table': 'museum_link',
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
                'get_latest_by': 'created',
            },
        ),
    ]
