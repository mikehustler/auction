from rest_framework import serializers, viewsets
from bidRecorder.models import Auction
from bidRecorder.models import AuctionItem
from bidRecorder.models import Registrant


class AuctionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Auction
        fields = ('name', 'description')


class RegistrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registrant
        fields = ('first_name', 'last_name', 'street', 'city', 'prov', 'pc')


class AuctionItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuctionItem
        fields = ('name', 'description', 'fmv', 'opening_bid', 'auction', 'donor')

# ---------------------------------------------------------------------------------------

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer


class RegistrantViewSet(viewsets.ModelViewSet):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer


class AuctionItemViewSet(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer
