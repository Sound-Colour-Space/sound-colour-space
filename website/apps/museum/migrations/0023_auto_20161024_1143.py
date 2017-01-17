# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-24 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0022_entry_doc_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', django_extensions.db.fields.UUIDField(blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, verbose_name='slug')),
            ],
            options={
                'ordering': ('-title',),
                'db_table': 'museum_experiment',
                'verbose_name': 'experiment',
                'verbose_name_plural': 'experiments',
            },
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'get_latest_by': 'created', 'ordering': ('doc_id', 'date'), 'verbose_name': 'diagram', 'verbose_name_plural': 'diagrams'},
        ),
    ]