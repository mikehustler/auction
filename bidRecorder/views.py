from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def listUsers(request):
    return HttpResponse("list of users")

def listItems(request):
    return HttpResponse("list of items")
