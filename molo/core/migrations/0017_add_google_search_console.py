# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-06 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_richtext_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='google_search_console',
            field=models.CharField(blank=True, help_text='The Google Search Console verification code', max_length=255, null=True, verbose_name='Google Search Console'),
        ),
    ]
