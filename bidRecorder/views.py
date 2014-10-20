from django.http import HttpResponse
from bidRecorder.models import AuctionItem

def index(request):
    return HttpResponse("hello world")

def listUsers(request):
    return HttpResponse("list of users")

def listItems(request):
    itemList = AuctionItem.objects.order_by('name')
    output = ', '.join([p.name for p in itemList])
    return HttpResponse("list of items: " + output)
