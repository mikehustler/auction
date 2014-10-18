from django.conf.urls import patterns, url
from bidRecorder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.listUsers, name='listUsers'),
    url(r'^items/$', views.listItems, name='listItems'),
)

