from django.contrib import admin

from bidRecorder.models import Auction
from bidRecorder.models import AuctionItem
from bidRecorder.models import Registrant

admin.site.register(Auction)
admin.site.register(AuctionItem)
admin.site.register(Registrant)
