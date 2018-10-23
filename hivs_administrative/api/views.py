from django.apps import apps
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import AreaTypeSerializer, AreaSerializer, AreaCountSerializer, StreetSerializer


AreaType = apps.get_registered_model('hivs_administrative', 'AreaType')
Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AdmistrativePagination(PageNumberPagination):
    page_size = 1000


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
    pagination_class = AdmistrativePagination

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

    group_by_related_models = {
        'profiles': {
            'rel_cls': apps.get_registered_model('hivs_clients', 'Profile'),
            'rel_field': 'area',
            'count_attr': 'count'
        },
    }

    @action(detail=False, methods=['get'])
    def related_count(self, request, *args, **kwargs):
        """Count related items."""
        by = request.query_params.get('by')

        if not by:
            return Response({'detail': _('Missing parameter `by`.')}, status.HTTP_400_BAD_REQUEST)

        if by not in self.group_by_related_models:
            return Response({'detail': _('Invalid `by` value.')}, status.HTTP_400_BAD_REQUEST)

        grouping = self.group_by_related_models[by]

        queryset = self.filter_queryset(self.get_queryset())
        queryset = Area.objects.add_related_count(
                queryset,
                grouping['rel_cls'],
                grouping['rel_field'],
                grouping['count_attr'],
                cumulative=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AreaCountSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AreaCountSerializer(queryset, many=True)
        return Response(serializer.data)


class StreetViewSet(viewsets.ModelViewSet):
    """
    Administrative Areas.
    """
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    pagination_class = AdmistrativePagination
