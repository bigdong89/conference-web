# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20170702_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
