# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 10:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0007_paperapplication_extra_info'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usergroups', '0004_auto_20160905_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='cfp.PaperApplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usergroup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='usergroups.UserGroup')),
            ],
        ),
    ]
