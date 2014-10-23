from django.conf.urls import patterns, url
from bidRecorder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^registry/$', views.listRegistrants, name='listRegistrants'),
    url(r'^items/$', views.listItems, name='listItems'),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name='item'),
    url(r'^registrant/(?P<registrant_id>\d+)/$', views.registrant, name='registrant'),)






