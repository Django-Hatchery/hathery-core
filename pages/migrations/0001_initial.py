# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-16 12:57
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_title', models.CharField(max_length=200)),
                ('page_title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='publish')),
                ('body', ckeditor.fields.RichTextField()),
                ('publish', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='page')),
            ],
            options={
                'ordering': ('page_title',),
            },
        ),
    ]
