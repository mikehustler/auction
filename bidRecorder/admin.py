from django.contrib import admin

from bidRecorder.models import Auction
from bidRecorder.models import AuctionItem
from bidRecorder.models import Registrant
from bidRecorder.models import Address

admin.site.register(Auction)
admin.site.register(AuctionItem)
admin.site.register(Registrant)
admin.site.register(Address)
