from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from bidRecorder.serializers import AuctionViewSet
from bidRecorder.serializers import RegistrantViewSet
from bidRecorder.serializers import AuctionItemViewSet
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'registry', RegistrantViewSet)
router.register(r'items', AuctionItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^auction/', include('bidRecorder.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

