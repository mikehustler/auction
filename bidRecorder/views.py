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
    auction = Auction.objects.get(pk=auction_id)
    context = {
        'itemList': itemList,
        'auctionId': auction_id,
        'auction': auction
    }
    return render(request, 'bidRecorder/items.html', context)


def auction(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    context = {'auction': auction}
    return render(request, 'bidRecorder/auction.html', context)


def deleteAuction(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    auction.delete()
    # cascade delete follwing auction delete also deletes items
    return HttpResponseRedirect(reverse('listAuctions'))


def item(request, item_id):
    item = AuctionItem.objects.get(pk=item_id)
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


def newAuctionDetail(request):
    context = {}
    return render(request, 'bidRecorder/newauctiondetail.html', context)


def newRegistrantDetail(request):
    context = {}
    return render(request, 'bidRecorder/newregistrantdetail.html', context)


def editRegistrantDetail(request, registrant_id):
    print >> sys.stderr, '(entry)registrant_id: ' + str(registrant_id)
    registrant = Registrant.objects.get(pk=registrant_id)
    context = {'registrant': registrant}
    print >> sys.stderr, '(entry)registrant_id: ' + str(registrant)
    return render(request, 'bidRecorder/newregistrantdetail.html', context)


def addRegistrant(request, registrant_id=None):
    print >> sys.stderr, '(entry)registrant_id: ' + str(registrant_id)
    registrant = None

    try:
      registrant = Registrant.objects.get(pk=registrant_id)
      print >> sys.stderr, '(try) registrant_id: ' + str(registrant.id)
    except: Registrant.DoesNotExist

    if registrant :
      print >> sys.stderr, 'does exist'
      registrant.first_name = request.POST['first_name']
      registrant.last_name = request.POST['last_name']
      registrant.street = request.POST['street']
      registrant.city = request.POST['city']
      registrant.prov = request.POST['prov']
      registrant.pc = request.POST['pc']

      registrant.save()
    else :
      print >> sys.stderr, 'does not exist'
      registrant = Registrant.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        street = request.POST['street'],
        city = request.POST['city'],
        prov = request.POST['prov'],
        pc = request.POST['pc'],
    )
    return HttpResponseRedirect(reverse('listRegistrants'))


def deleteRegistrant(request, registrant_id):

    registrant = Registrant.objects.get(pk=registrant_id)
    registrant.delete()
    return HttpResponseRedirect(reverse('listRegistrants'))


def addItem(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    newItem = auction.auctionitem_set.create(
        auction = auction,
        name=request.POST['name'],
        description=request.POST['description'],
        fmv = request.POST['fmv'],
        opening_bid = request.POST['openingBid'],
        donor = Registrant.objects.get(),
    )
    context = {'auctionId': auction_id}
    return HttpResponseRedirect(reverse('item', args=(newItem.id,)))


def deleteItem(request, item_id):

    item = AuctionItem.objects.get(pk=item_id)
    auction_id = item.auction.id
    item.delete()
    return HttpResponseRedirect(reverse('listItems', args=(auction_id,)))


def addAuction(request):
    auction = Auction.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
    )
    return HttpResponseRedirect(reverse('listAuctions'))
