from django.conf.urls import patterns, url
from bidRecorder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^auctions/$', views.listAuctions, name='listAuctions'),
    url(r'^newauctiondetail/$', views.newAuctionDetail, name='newAuctionDetail'),
    url(r'^addAuction/$', views.addAuction, name='addAuction'),
    url(r'^deleteAuction/(?P<auction_id>\d+)/$', views.deleteAuction, name='deleteAuction'),

    url(r'^registry/$', views.listRegistrants, name='listRegistrants'),
    url(r'^registrant/(?P<registrant_id>\d+)/$', views.registrant, name='registrant'),

    url(r'^items/(?P<auction_id>\d+)/$', views.listItems, name='listItems'),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name='item'),
    url(r'^newitemdetail/(?P<auction_id>\d+)/$', views.newItemDetail, name='newItemDetail'),
    url(r'^additem/(?P<auction_id>\d+)/$', views.addItem, name='addItem'),
    url(r'^deleteitem/(?P<item_id>\d+)/$', views.deleteItem, name='deleteItem'),
)
