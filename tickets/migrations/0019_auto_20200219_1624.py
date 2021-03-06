# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-19 16:24
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('tickets', '0018_ticket_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='tags',
        ),
        migrations.AddField(
            model_name='ticket',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
