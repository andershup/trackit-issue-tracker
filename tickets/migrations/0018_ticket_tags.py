# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-19 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0017_ticket_submitted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
