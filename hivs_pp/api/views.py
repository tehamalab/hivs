from django.apps import apps
from rest_framework import viewsets
from .serializers import CategorySerializer, ServiceSerializer, DeliverySerializer


Category = apps.get_registered_model('hivs_pp', 'Category')
Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')


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
        'gender': ['exact'],
        'age': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'services': ['exact', 'in'],
        'services__category': ['exact'],
        'services__category__name': ['exact', 'iexact'],
        'referral_made': ['exact'],
        'referral_successful': ['exact'],
        'provider': ['exact'],
    }
    ordering = ['-date']
