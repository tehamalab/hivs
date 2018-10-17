from django.apps import apps
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProfileSerializer


Profile = apps.get_model('hivs_clients', 'Profile')


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Clients Profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_fields = [
        'acquisition_date',
        'area',
        'area__name',
        'street',
        'street__name',
        'education_level',
        'occupation',
        'gender',
        'gender__name',
        'martial_status',
        'martial_status__name',
    ]

    group_by_fields = [
        'acquisition_date',
        'area',
        'area__name',
        'street',
        'street__name',
        'education_level',
        'occupation',
        'gender',
        'gender__name',
        'martial_status',
        'martial_status__name',
    ]

    ordering_fields = [
        'acquisition_date',
        'area',
        'area__name',
        'street',
        'street__name',
        'education_level',
        'occupation',
        'gender',
        'gender__name',
        'martial_status',
        'martial_status__name',
    ]

    @action(detail=False, methods=['get'])
    def total(self, request, *args, **kwargs):
        """Get total number of clients profiles."""
        queryset = self.filter_queryset(self.get_queryset())
        data = {'count': queryset.count()}
        return Response(data)

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        """Count clients profiles by group."""

        groups = request.query_params.getlist('group')

        if not groups:
            return Response({'detail': _('Missing group.')}, status.HTTP_400_BAD_REQUEST)

        if not set(groups).issubset(self.group_by_fields):
            return Response({'detail': _('Invalid group.')}, status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset())
        data = queryset.values(*groups).annotate(count=Count('*'))[:100]
        return Response(data)
