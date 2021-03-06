# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-23 18:52
from __future__ import unicode_literals

import common.storage
from django.db import migrations, models
import museum.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0044_auto_20170223_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, verbose_name='slug')),
                ('cover', models.ImageField(blank=True, null=True, storage=common.storage.DataStorage(base_url=b'/media/experiments/', location=b'/home/stahl/icst/soundcolourspace/sound-colour-space/website/media/experiments'), upload_to=museum.models.generate_data_path, verbose_name='cover')),
                ('url', models.URLField(blank=True, null=True, verbose_name='url')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'ordering': ('title',),
                'db_table': 'museum_exhibition',
                'verbose_name': 'exhibition',
                'verbose_name_plural': 'exhibition',
            },
        ),
    ]
