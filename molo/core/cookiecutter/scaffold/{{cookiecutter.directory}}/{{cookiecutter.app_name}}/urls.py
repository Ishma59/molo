import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from molo.core.views import upload_file, download_file

# implement CAS URLs in a production setting
if settings.ENABLE_SSO:
    urlpatterns = patterns(
        '',
        url(r'^admin/login/', 'django_cas_ng.views.login'),
        url(r'^admin/logout/', 'django_cas_ng.views.logout'),
        url(r'^admin/callback/', 'django_cas_ng.views.callback'),
    )
else:
    urlpatterns = patterns('', )

urlpatterns += patterns(
    '',
    url(r'^django-admin/upload_media/', upload_file,
        name='molo_upload_media'),
    url(r'^django-admin/download_media/', download_file,
        name='molo_download_media'),
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

{% for app_name, regex in cookiecutter.include %}
    url(r'{{regex}}',
        include('{{app_name}}.urls',
                namespace='{{app_name}}',
                app_name='{{app_name}}')),
{% endfor %}
    url(r"^mote/", include("mote.urls", namespace="mote")),
    url(r'', include('molo.core.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'', include(wagtail_urls)),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL + 'images/',
        document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
