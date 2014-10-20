from django.http import HttpResponse
from django.template import RequestContext, loader
from bidRecorder.models import AuctionItem

def index(request):
    return HttpResponse("hello world")

def listUsers(request):
    return HttpResponse("list of users")

def listItems(request):
    itemList = AuctionItem.objects.order_by('name')
    template = loader.get_template('bidRecorder/items.html')
    context = RequestContext(request, {
        'itemList': itemList,
    })
    return HttpResponse(template.render(context))
