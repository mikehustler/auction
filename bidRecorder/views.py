from django.http import HttpResponse
from django.shortcuts import render
from bidRecorder.models import Auction
from bidRecorder.models import AuctionItem
from bidRecorder.models import Registrant

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
    }
    return render(request, 'bidRecorder/items.html', context)

def auction(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    context = {'auction': auction}
    return render(request, 'bidRecorder/auction.html', context)

def item(request, item_id):
    item = AuctionItem.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'bidRecorder/item.html', context)

def registrant(request, registrant_id):
    registrant = Registrant.objects.get(pk=registrant_id)
    context = {'registrant': registrant}
    return render(request, 'bidRecorder/registrant.html', context)
