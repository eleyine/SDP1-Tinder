from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from sdp1_tinder import views

from django.contrib import admin

# from djrill import DjrillAdminSite

# admin.site = DjrillAdminSite()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/', include('app.api.urls')),
)

urlpatterns += i18n_patterns(
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^app/', include('app.urls')),
)
# Javascript Internationalization Support
from django.views.i18n import javascript_catalog

js_info_dict = {
    'packages': (
            'app',
        ),
}


urlpatterns = i18n_patterns(
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='django.views.i18n.javascript_catalog'),
) + urlpatterns

# Debug 
from django.conf import settings
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns(
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
        )