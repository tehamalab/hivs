from django.apps import apps
from rest_framework import viewsets
from .serializers import AreaTypeSerializer, AreaSerializer, StreetSerializer


AreaType = apps.get_registered_model('hivs_administrative', 'AreaType')
Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AreaTypeViewSet(viewsets.ModelViewSet):
    """
    Administrative Areas.
    """
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    Administrative Areas.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    filterset_fields = {
        'name': ['exact', 'iexact', 'icontains'],
        'parent': ['exact'],
        'level': ['exact'],
        'area_type': ['exact'],
        'area_type__name': ['exact', 'iexact'],
        'population': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'population_male': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'population_female': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'households': ['exact', 'lt', 'lte', 'gt', 'gte'],
    }

    ordering_fields = [
        'name',
        'parent',
        'population',
        'population_male',
        'population_female',
        'househoulds',
    ]


class StreetViewSet(viewsets.ModelViewSet):
    """
    Administrative Areas.
    """
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
