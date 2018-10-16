from django.urls import path, include
from rest_framework import routers
from hivs_clients.api.views import ProfileViewSet


router = routers.DefaultRouter()
router.register(r'clients/profiles', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('_auth/', include('rest_framework.urls'))
]
