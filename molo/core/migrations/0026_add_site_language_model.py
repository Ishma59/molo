# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0024_alter_page_content_type_on_delete_behaviour'),
        ('core', '0025_add_translation_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(help_text='Site language', max_length=255, verbose_name='language name', choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese'), (b'zu', 'Zulu'), (b'xh', 'Xhosa'), (b'st', 'Sotho'), (b've', 'Venda'), (b'tn', 'Tswana'), (b'ts', 'Tsonga'), (b'ss', 'Swati'), (b'nr', 'Ndebele')])),
                ('is_main_language', models.BooleanField(default=False, verbose_name='main Language', editable=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='active Language')),
            ],
            options={
                'verbose_name': 'Language',
            },
        ),
        migrations.RemoveField(
            model_name='articlepage',
            name='language',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='language',
        ),
        migrations.RemoveField(
            model_name='languagepage',
            name='main_language',
        ),
        migrations.RemoveField(
            model_name='sectionpage',
            name='language',
        ),
        migrations.AlterField(
            model_name='pagetranslation',
            name='page',
            field=models.ForeignKey(related_name='translations', to='wagtailcore.Page', on_delete=models.SET_NULL),
        ),
        migrations.AddField(
            model_name='languagerelation',
            name='language',
            field=models.ForeignKey(related_name='+', to='core.SiteLanguage', on_delete=models.SET_NULL),
        ),
        migrations.AddField(
            model_name='languagerelation',
            name='page',
            field=models.ForeignKey(related_name='languages', to='wagtailcore.Page', on_delete=models.SET_NULL),
        ),
    ]
