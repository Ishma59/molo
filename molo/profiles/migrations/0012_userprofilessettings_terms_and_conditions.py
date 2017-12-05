# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-10 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('profiles', '0011_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilessettings',
            name='terms_and_conditions',
            field=models.ForeignKey(blank=True, help_text='Choose a footer page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
