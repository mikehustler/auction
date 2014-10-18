from django.contrib import admin

from bidRecorder.models import AuctionItem
from bidRecorder.models import RegisteredPerson
from bidRecorder.models import Address

admin.site.register(AuctionItem)
admin.site.register(RegisteredPerson)
admin.site.register(Address)
