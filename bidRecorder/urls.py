from django.conf.urls import patterns, url
from bidRecorder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^auctions/$', views.listAuctions, name='listAuctions'),
    url(r'^registry/$', views.listRegistrants, name='listRegistrants'),
    url(r'^items/(?P<auction_id>\d+)/$', views.listItems, name='listItems'),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name='item'),
    url(r'^registrant/(?P<registrant_id>\d+)/$', views.registrant, name='registrant'),
#    url(r'^items/additem/$', views.addItem, name='addItem'),
)






