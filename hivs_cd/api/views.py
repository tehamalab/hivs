from django.apps import apps
from rest_framework import viewsets
from .serializers import CenterSerializer, PurposeSerializer, CondomDistributionSerializer


Center = apps.get_registered_model('hivs_cd', 'Center')
Purpose = apps.get_registered_model('hivs_cd', 'Purpose')
CondomDistribution = apps.get_registered_model('hivs_cd', 'CondomDistribution')


class CenterViewSet(viewsets.ModelViewSet):
    """
    Condom Distribution Centers.
    """
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
    filterset_fields = {
        'name': ['exact', 'iexact', 'icontains'],
        'center_no': ['exact', 'iexact'],
        'area': ['exact'],
        'area__name': ['exact', 'iexact'],
        'street': ['exact'],
        'street__name': ['exact', 'iexact'],
    }
    ordering = ['name']


class PurposeViewSet(viewsets.ModelViewSet):
    """
    Condom Distribution Purpose.
    """
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    ordering = ['name']


class CondomDistributionViewSet(viewsets.ModelViewSet):
    """
    Condom Distribution.
    """
    queryset = CondomDistribution.objects.prefetch_related('education_topics')
    serializer_class = CondomDistributionSerializer
    filterset_fields = {
        'date': ['exact', 'lt', 'lte', 'gt', 'gte', 'year',
                 'month', 'week', 'week_day', 'quarter'],
        'gender': ['exact'],
        'gender__name': ['exact', 'iexact'],
        'age': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'attendance_type': ['exact'],
        'condoms_male_count': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'condoms_female_count': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'referral_made': ['exact'],
        'referral_type': ['exact'],
        'education_delivered': ['exact'],
        'education_topics': ['exact'],
    }
    ordering = ['-date']
