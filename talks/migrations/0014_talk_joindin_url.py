# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0013_talk_starts_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='joindin_url',
            field=models.URLField(blank=True, help_text='URL to the event on JoindIn API.'),
        ),
    ]
