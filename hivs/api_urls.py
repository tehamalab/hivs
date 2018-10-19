from django.urls import path, include
from rest_framework import routers
from hivs_clients.api.views import ProfileViewSet
from hivs_administrative.api.views import AreaTypeViewSet, AreaViewSet, StreetViewSet


router = routers.DefaultRouter()
router.register(r'administrative/area-types', AreaTypeViewSet)
router.register(r'administrative/areas', AreaViewSet)
router.register(r'administrative/streets', StreetViewSet)
router.register(r'clients/profiles', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('_auth/', include('rest_framework.urls'))
]
