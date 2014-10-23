from django.http import HttpResponse
from django.shortcuts import render
from bidRecorder.models import AuctionItem
from bidRecorder.models import Registrant

def index(request):
    return render(request, 'bidRecorder/index.html')


def listRegistrants(request):
    registry = Registrant.objects.order_by('last_name')
    context = {
        'registry': registry,
    }
    return render(request, 'bidRecorder/registry.html', context)

def listItems(request):
    itemList = AuctionItem.objects.order_by('name')
    context = {
        'itemList': itemList,
    }
    return render(request, 'bidRecorder/items.html', context)

def item(request, item_id):
    item = AuctionItem.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'bidRecorder/item.html', context)

def registrant(request, registrant_id):
    registrant = Registrant.objects.get(pk=registrant_id)
    context = {'registrant': registrant}
    return render(request, 'bidRecorder/registrant.html', context)
