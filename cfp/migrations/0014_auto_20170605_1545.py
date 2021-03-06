# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 13:45
from __future__ import unicode_literals

import cfp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0013_auto_20170523_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='about',
            field=models.TextField(help_text='Describe yourself in 140 characters or fewer. Plain text only. [Public]', verbose_name='About you'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='biography',
            field=models.TextField(help_text='Who are you? Where have you worked? What are your professional interests? Up to 10 sentences, use Markdown. [Public]', verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='image',
            field=models.ImageField(help_text='Please upload a picture of yourself which we may use for our web site and publications. Make it a square PNG of at least 400x400px. [Public]', max_length=255, upload_to=cfp.models.get_applicant_avatar_path, verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='speaker_experience',
            field=models.TextField(blank=True, help_text="If you've given talks at other events, please list them.Videos which show your english speaking skills are very helpful. Use markdown.", verbose_name='Speaker experience'),
        ),
    ]
