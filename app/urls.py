from django.conf.urls import patterns, url
from app import views
 
urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    url(r'^api/users/$', views.api.user_list),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.api.user_detail),
) 