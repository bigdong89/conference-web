# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-08 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_create_past_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='events.Event'),
        ),
    ]
