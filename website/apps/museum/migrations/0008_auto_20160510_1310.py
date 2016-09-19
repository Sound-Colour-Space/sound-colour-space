# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 11:10
from __future__ import unicode_literals

import common.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import museum.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museum', '0007_auto_20160510_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', django_extensions.db.fields.UUIDField(blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(blank=True, null=True, storage=common.storage.DataStorage(base_url=b'/media/data/', location=b'/home/stahl/icst/soundcolourspace/soundcolourspace/website/media/data'), upload_to=museum.models.generate_data_path, verbose_name='image')),
                ('year', models.CharField(blank=True, max_length=200, null=True, verbose_name='year')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='subtitle')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='museums_entries', to='museum.Author')),
                ('link', models.ManyToManyField(blank=True, related_name='museums_entries', to='museum.Link')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='museums_entries', to='museum.Source')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='museums_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'db_table': 'museum_entry',
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
                'get_latest_by': 'created',
            },
        ),
        migrations.RemoveField(
            model_name='museumsresource',
            name='author',
        ),
        migrations.RemoveField(
            model_name='museumsresource',
            name='link',
        ),
        migrations.RemoveField(
            model_name='museumsresource',
            name='source',
        ),
        migrations.RemoveField(
            model_name='museumsresource',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='museumsresource',
            name='uploader',
        ),
        migrations.DeleteModel(
            name='MuseumsResource',
        ),
    ]
