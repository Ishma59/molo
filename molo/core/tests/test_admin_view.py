from django.test import TestCase
from django.contrib.auth.models import User

from molo.core.models import (
    Main, SiteLanguageRelation, Languages,
    ArticlePage, ArticlePageTags)
from molo.core.tests.base import MoloTestCaseMixin


class TestAdminView(TestCase, MoloTestCaseMixin):
    def setUp(self):
        self.mk_main()
        main = Main.objects.all().first()
        self.english = SiteLanguageRelation.objects.create(
            language_setting=Languages.for_site(main.get_site()),
            locale='en',
            is_active=True)

        self.french = SiteLanguageRelation.objects.create(
            language_setting=Languages.for_site(main.get_site()),
            locale='fr',
            is_active=True)

        self.yourmind = self.mk_section(
            self.section_index, title='Your Mind')

        self.yourmind_fr = self.mk_section_translation(
            self.yourmind, self.french, title='Your mind in french')

        self.mk_main2()
        self.main2 = Main.objects.all().last()
        self.language_setting2 = Languages.objects.create(
            site_id=self.main2.get_site().pk)
        self.english2 = SiteLanguageRelation.objects.create(
            language_setting=self.language_setting2,
            locale='en',
            is_active=True)

        self.spanish = SiteLanguageRelation.objects.create(
            language_setting=self.language_setting2,
            locale='es',
            is_active=True)

        self.yourmind2 = self.mk_section(
            self.section_index2, title='Your mind2')

    def test_articles_appears_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.mk_article(self.yourmind)
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/'
        )
        self.assertContains(response, 'Test page 0')

    def test_section_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.mk_article(self.yourmind)
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/'
        )
        self.assertContains(response, 'Your Mind')

    def test_parent_section_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.yourmind_sub = self.mk_section(
            self.yourmind, title='Your mind subsection')
        self.mk_article(self.yourmind_sub)
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/'
        )
        self.assertContains(response, 'Your Mind')
        self.assertContains(response, 'Your mind subsection')

    def test_article_tags_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        article = self.mk_article(self.yourmind, title='article')
        article.tags.add("the tag")
        article.save_revision().publish()
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/'
        )
        self.assertContains(response, 'the tag')

    def test_status_custom_filter_published_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.mk_articles(self.yourmind)
        self.article2 = ArticlePage.objects.get(title="Test page 1")
        self.article2.unpublish()
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/?status=published'
        )
        self.assertContains(response, 'Test page 0')
        self.assertNotContains(response, 'Test page 1')

    def test_status_custom_filter_in_review_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.mk_articles(self.yourmind)
        self.article2 = ArticlePage.objects.get(title="Test page 1")
        self.article2.save_revision(submitted_for_moderation=True)
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/?status=in_review'
        )
        self.assertNotContains(response, 'Test page 0')
        self.assertContains(response, 'Test page 1')

    def test_status_custom_filter_draft_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.mk_articles(self.yourmind)
        self.article2 = ArticlePage.objects.get(title="Test page 1")
        self.article2.unpublish()
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/?status=draft'
        )
        self.assertNotContains(response, 'Test page 0')
        self.assertContains(response, 'Test page 1')

    def test_status_custom_filter_sections_in_admin_view(self):
        User.objects.create_superuser(
            username='testuser', password='password', email='test@email.com')
        self.client.login(username='testuser', password='password')
        self.mk_articles(self.yourmind)
        self.article2 = ArticlePage.objects.get(title="Test page 1")
        self.article2.unpublish()
        response = self.client.get(
            '/admin/core/articlepagelanguageproxy/?section=%d' %
            self.yourmind.id
        )
        self.assertContains(response, 'Test page 0')
        self.assertContains(response, 'Test page 1')
