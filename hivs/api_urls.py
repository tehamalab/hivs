from django.urls import path, include
from rest_framework import routers
from hivs_administrative.api.views import AreaTypeViewSet, AreaViewSet, StreetViewSet
from hivs_clients.api.views import ProfileViewSet
from hivs_pp.api.views import CategoryViewSet, ServiceViewSet, DeliveryViewSet, DeliveryPivotViewSet


router = routers.DefaultRouter()
router.register(r'administrative/area-types', AreaTypeViewSet)
router.register(r'administrative/areas', AreaViewSet)
router.register(r'administrative/streets', StreetViewSet)
router.register(r'clients/profiles', ProfileViewSet)
router.register(r'prevention/categories', CategoryViewSet)
router.register(r'prevention/services', ServiceViewSet)
router.register(r'prevention/deliveries', DeliveryViewSet)
router.register(r'prevention/pivot', DeliveryPivotViewSet, 'delivery-pivot')


urlpatterns = [
    path('', include(router.urls)),
    path('_auth/', include('rest_framework.urls'))
]
