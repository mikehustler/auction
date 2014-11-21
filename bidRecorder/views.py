from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from bidRecorder.models import Auction
from bidRecorder.models import AuctionItem
from bidRecorder.models import Registrant
import sys

def index(request):
    return render(request, 'bidRecorder/index.html')


def listAuctions(request):
    auctionList = Auction.objects.order_by('name')
    context = {
        'auctionList': auctionList,
    }
    return render(request, 'bidRecorder/auctions.html', context)


def listRegistrants(request):
    registry = Registrant.objects.order_by('last_name')
    context = {
        'registry': registry,
    }
    return render(request, 'bidRecorder/registry.html', context)


def listItems(request, auction_id):
    itemList = AuctionItem.objects.filter(auction=auction_id).order_by('name')
    context = {
        'itemList': itemList,
        'auctionId': auction_id,
    }
    return render(request, 'bidRecorder/items.html', context)


def auction(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    context = {'auction': auction}
    return render(request, 'bidRecorder/auction.html', context)


def item(request, item_id):
    item = AuctionItem.objects.get(pk=item_id)
    print >>sys.stderr, 'item_id: ' + item_id
    context = {'item': item}
    return render(request, 'bidRecorder/item.html', context)


def registrant(request, registrant_id):
    registrant = Registrant.objects.get(pk=registrant_id)
    context = {'registrant': registrant}
    return render(request, 'bidRecorder/registrant.html', context)


def newItemDetail(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    context = {'auction': auction}
    return render(request, 'bidRecorder/newitemdetail.html', context)


def addItem(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    newItem = auction.auctionitem_set.create(
        auction = auction,
        name=request.POST['name'],
        description=request.POST['description'],
        fmv = request.POST['fmv'],
        opening_bid = request.POST['openingBid'],
        donor = Registrant.objects.get(pk=1),
    )
    context = {'auctionId': auction_id}
    return HttpResponseRedirect(reverse('item', args=(newItem.id,)))

def deleteItem(request, item_id):

    print >>sys.stderr, 'item_id: ' + item_id
    
    item = AuctionItem.objects.get(pk=item_id)
    auction_id = item.auction.id
    item.delete()
    return HttpResponseRedirect(reverse('listItems', args=(auction_id,)))
