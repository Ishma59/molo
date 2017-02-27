# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def convert_languages_to_site_language_relation(apps, schema_editor):
    from molo.core.models import SiteLanguage, SiteLanguageRelation Main
    main = Main.objects.all().first()
    if main:
        site = main.get_site()
        if site:
            language_setting, _ = Languages.objects.get_or_create(
                site_id=site.pk)
            for language in SiteLanguage.objects.all():
                SiteLanguageRelation.objects.create(
                    language_setting=language_setting,
                    locale=language.locale,
                    is_active=language.is_active)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_languages_sitelanguagerelation'),
    ]

    operations = [
        migrations.RunPython(convert_languages_to_site_language_relation),
    ]
