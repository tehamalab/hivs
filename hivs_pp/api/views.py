from django.apps import apps
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CategorySerializer, ServiceSerializer, DeliverySerializer


Category = apps.get_registered_model('hivs_pp', 'Category')
Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')
Area = apps.get_registered_model('hivs_administrative', 'Area')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Prevention interventions Categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering = ['name']


class ServiceViewSet(viewsets.ModelViewSet):
    """
    Prevention interventions Services.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = {
        'category': ['exact'],
        'category__name': ['exact', 'iexact'],
        'name': ['exact', 'iexact', 'icontains'],
        'description': ['icontains'],
        'is_confidential': ['exact'],
    }
    ordering = ['name']


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    Prevention interventions Service Delivery.
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    filterset_fields = {
        'date': ['exact', 'lt', 'lte', 'gt', 'gte', 'year',
                 'month', 'week', 'week_day', 'quarter'],
        'time': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'client': ['exact'],
        'area': ['exact'],
        'area__name': ['exact', 'iexact'],
        'gender': ['exact'],
        'age': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'services': ['exact'],
        'services__category': ['exact'],
        'services__category__name': ['exact', 'iexact'],
        'referral_made': ['exact'],
        'referral_successful': ['exact'],
        'provider': ['exact'],
    }
    ordering = ['-date']
    count_by = [
        'date',
        'gender',
        'gender__name',
        'age',
        'area',
        'area__name',
        'related_areas',
        'services',
        'services__name',
        'services__category',
        'services__category__name',
        'referral_made',
        'referral_successful',
        'provider',
    ]

    @action(detail=False, methods=['get'])
    def total(self, request, *args, **kwargs):
        """Total number of service deliveries."""
        queryset = self.filter_queryset(self.get_queryset())
        data = {'count': queryset.count()}
        return Response(data)

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        """Count service deliveries by group."""

        area_level = None

        by = set(request.query_params.getlist('by'))

        if not by:
            return Response({'detail': _('Missing parameter `by`.')}, status.HTTP_400_BAD_REQUEST)

        if not by.issubset(self.count_by):
            return Response({'detail': _('Invalid `by` value.')}, status.HTTP_400_BAD_REQUEST)

        if 'related_areas' in by and request.query_params.get('area_level'):
            try:
                area_level = int(request.query_params.get('area_level', ''))
            except ValueError:
                return Response(
                    {'detail': _('Invalid or Missing `area_level`.')},
                    status.HTTP_400_BAD_REQUEST
                )

        if area_level is not None:
            by.remove('related_areas')
            by |= {'area_id', 'area_name'}

        # ordering causes duplicate entries if not part of grouping. See
        # https://docs.djangoproject.com/en/dev/topics/db/aggregation/#interaction-with-default-ordering-or-order-by
        self.ordering = by

        queryset = self.filter_queryset(self.get_queryset())

        if area_level is not None:
            areas = Area.objects.filter(level=area_level).values_list('id', flat=True)
            queryset = queryset\
                .filter(related_areas_ids__overlap=list(areas))\
                .extra(select={'area_id': 'related_areas_ids[%s]'}, select_params=(area_level + 1,))\
                .extra(select={'area_name': 'related_areas[%s]'}, select_params=(area_level + 1,))
            print(by)

        data = queryset.values(*by).annotate(count=Count('id'))[:100]
        return Response(data)
