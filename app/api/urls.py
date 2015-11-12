from django.conf.urls import patterns, url
from app.api import handlers
 
urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    url(r'users/$', handlers.user_list),
    url(r'users/(?P<pk>[0-9]+)/$', handlers.user_detail),
) 