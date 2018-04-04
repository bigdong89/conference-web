# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-04 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('talks', '0001_initial'), ('talks', '0002_auto_20150601_0926'), ('talks', '0003_talk_slug'), ('talks', '0004_talk_keynote'), ('talks', '0005_auto_20150905_1220'), ('talks', '0006_talk_co_presenter'), ('talks', '0007_talk_slides_url'), ('talks', '0008_auto_20151127_0808'), ('talks', '0009_talk_rate_url'), ('talks', '0010_auto_20160910_1700'), ('talks', '0011_auto_20170519_0944'), ('talks', '0012_talk_event'), ('talks', '0013_talk_starts_at'), ('talks', '0014_talk_joindin_url')]

    initial = True

    dependencies = [
        ('cfp', '0004_auto_20150531_2008'),
        ('sponsors', '0008_sponsor_order'),
        ('events', '0004_auto_20170516_1156'),
        ('cfp', '0005_paperapplication_exclude'),
        ('usergroups', '0005_voteaudit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('about', models.TextField(blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('duration', models.CharField(blank=True, choices=[('25', '25 Minutes'), ('45', '45 Minutes')], max_length=255, null=True)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='talk', to='cfp.PaperApplication')),
                ('skill_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cfp.AudienceSkillLevel')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('keynote', models.BooleanField(default=False)),
                ('is_community_chosen', models.BooleanField(default=False)),
                ('co_presenter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='co_talks', to='cfp.Applicant')),
                ('slides_url', models.URLField(blank=True)),
                ('youtube_id', models.CharField(blank=True, max_length=20)),
                ('rate_url', models.URLField(blank=True)),
                ('sponsor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sponsored_talks', to='sponsors.Sponsor')),
                ('usergroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chosen_talks', to='usergroups.UserGroup')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='talks', to='events.Event')),
                ('starts_at', models.DateTimeField(blank=True, null=True)),
                ('joindin_url', models.URLField(blank=True, help_text='URL to the event on JoindIn API.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
