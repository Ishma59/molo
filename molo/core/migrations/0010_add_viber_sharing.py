# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_add_new_social_sharing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettings',
            old_name='youtube_image',
            new_name='viber_image',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='youtube_sharing',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='viber_sharing',
            field=models.BooleanField(default=False, help_text='Enable this field to allow for sharing to Viber.', verbose_name='Viber'),
        ),
    ]
