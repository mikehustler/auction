from django.conf.urls import patterns, url
from bidRecorder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^auctions/$', views.listAuctions, name='listAuctions'),
    url(r'^newAuctionDetail/$', views.newAuctionDetail, name='newAuctionDetail'),
    url(r'^addAuction/$', views.addAuction, name='addAuction'),
    url(r'^editAuctionDetail/(?P<auction_id>\d+)/$', views.editAuctionDetail, name='editAuctionDetail'),
    url(r'^editAuction/(?P<auction_id>\d+)/$', views.editAuction, name='editAuction'),
    url(r'^deleteAuction/(?P<auction_id>\d+)/$', views.deleteAuction, name='deleteAuction'),


    url(r'^registry/$', views.listRegistrants, name='listRegistrants'),
    url(r'^registrant/(?P<registrant_id>\d+)/$', views.registrant, name='registrant'),
    url(r'^newRegistrantDetail/$', views.newRegistrantDetail, name='newRegistrantDetail'),
    url(r'^addRegistrant/$', views.addRegistrant, name='addRegistrant'),
    url(r'^editRegistrantDetail/(?P<registrant_id>\d+)/$', views.editRegistrantDetail, name='editRegistrantDetail'),
    url(r'^editRegistrant/(?P<registrant_id>\d+)/$', views.editRegistrant, name='editRegistrant'),
    url(r'^deleteRegistrant/(?P<registrant_id>\d+)/$', views.deleteRegistrant, name='deleteRegistrant'),


    url(r'^items/(?P<auction_id>\d+)/$', views.listItems, name='listItems'),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name='item'),
    url(r'^newItemDetail/(?P<auction_id>\d+)/$', views.newItemDetail, name='newItemDetail'),
    url(r'^addItem/(?P<auction_id>\d+)/$', views.addItem, name='addItem'),
    url(r'^editItemDetail/(?P<item_id>\d+)/$', views.editItemDetail, name='editItemDetail'),
    url(r'^editItem/(?P<item_id>\d+)/$', views.editItem, name='editItem'),
    url(r'^deleteItem/(?P<item_id>\d+)/$', views.deleteItem, name='deleteItem'),
)
