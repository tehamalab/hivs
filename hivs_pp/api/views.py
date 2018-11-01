import pandas as pd
from django.apps import apps
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.template.defaultfilters import slugify
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException, MethodNotAllowed
from rest_framework.decorators import action
from rest_framework_csv.renderers import CSVStreamingRenderer
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

    def parse_count_request(self, request):
        """
        Parse request parameter for counting actions.
        """

        by = set(request.query_params.getlist('by'))
        if not by:
            raise APIException(_('Missing parameter `by`.'), status.HTTP_400_BAD_REQUEST)
        if not by.issubset(self.count_by):
            raise APIException(_('Invalid `by` value.'), status.HTTP_400_BAD_REQUEST)

        area_level = None
        if 'related_areas' in by and request.query_params.get('area_level'):
            try:
                area_level = int(request.query_params.get('area_level', ''))
            except ValueError:
                raise APIException(
                    _('Invalid or Missing `area_level`.'),
                    status.HTTP_400_BAD_REQUEST
                )

        return {'by': by, 'area_level': area_level}

    def get_count(self, by, area_level=None):
        """Count service deliveries by group."""

        if area_level is not None:
            by.remove('related_areas')
            by |= {'area_id', 'area_name'}

        # ordering causes duplicate entries if not part of grouping. See
        # https://docs.djangoproject.com/en/dev/topics/db/aggregation/#interaction-with-default-ordering-or-order-by
        for i in self.ordering:
            if i not in by:
                self.ordering.remove(i)

        queryset = self.filter_queryset(self.get_queryset())

        if area_level is not None:
            areas = Area.objects.filter(level=area_level).values_list('id', flat=True)
            queryset = queryset\
                .filter(related_areas_ids__overlap=list(areas))\
                .extra(select={'area_id': 'related_areas_ids[%s]'}, select_params=(area_level + 1,))\
                .extra(select={'area_name': 'related_areas[%s]'}, select_params=(area_level + 1,))

        return queryset.values(*by).annotate(count=Count('id'))

    @action(detail=False, methods=['get'])
    def total(self, request, *args, **kwargs):
        """Total number of service deliveries."""
        queryset = self.filter_queryset(self.get_queryset())
        data = {'count': queryset.count()}
        return Response(data)

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        """Count service deliveries by group."""
        params = self.parse_count_request(request)
        return Response(self.get_count(params['by'], params['area_level']))


class DeliveryPivotViewSet(DeliveryViewSet):
    """
    Prevention interventions Service Delivery Pivot Table.
    """

    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVStreamingRenderer, )
    rows_fields = ['date', 'gender', 'age', 'area', 'area_name', 'services', 'referral_made',
                   'referral_successful']
    columns_fields = ['date', 'gender', 'age', 'area', 'services', 'referral_made',
                      'referral_successful', 'count']
    values_fields = ['count']
    aggregations = ['mean', 'sum', 'count']

    def parse_pivot_request(self, request):
        """Parse request parameter for pivot table generation."""
        rows = set(request.query_params.getlist('rows'))
        if not rows:
            raise APIException(_('Missing parameter `rows`.'), status.HTTP_400_BAD_REQUEST)
        if not rows.issubset(self.rows_fields):
            raise APIException(_('Invalid `rows` value.'), status.HTTP_400_BAD_REQUEST)

        columns = set(request.query_params.getlist('columns'))
        if not columns:
            raise APIException(_('Missing parameter `columns`.'), status.HTTP_400_BAD_REQUEST)
        if not columns.issubset(self.columns_fields):
            raise APIException(_('Invalid `columns` value.'), status.HTTP_400_BAD_REQUEST)

        values = set(request.query_params.getlist('values'))
        if not values:
            raise APIException(_('Missing parameter `values`.'), status.HTTP_400_BAD_REQUEST)
        if not values.issubset(self.values_fields):
            raise APIException(_('Invalid `values` value.'), status.HTTP_400_BAD_REQUEST)

        try:
            fill = int(self.request.query_params.get('fill', 0))
        except ValueError:
            raise APIException(_('Invalid `fill` value.'), status.HTTP_400_BAD_REQUEST)

        agg = request.query_params.get('aggregation', 'mean')
        if agg not in self.aggregations:
            raise APIException(_('Invalid `aggregation`.'), status.HTTP_400_BAD_REQUEST)

        totals_label = request.query_params.get('totals')
        if totals_label:
            include_totals = True
        else:
            include_totals = False

        return {
            'index': list(rows),
            'columns': list(columns),
            'values': list(values),
            'fill_value': fill,
            'margins': include_totals,
            'margins_name': totals_label,
            'aggfunc': agg,
        }

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def create(self, request):
        raise MethodNotAllowed(request.method)

    def retrieve(self, request, pk=None):
        raise MethodNotAllowed(request.method)

    def update(self, request, pk=None):
        raise MethodNotAllowed(request.method)

    def partial_update(self, request, pk=None):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, pk=None):
        raise MethodNotAllowed(request.method)

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        """Count and pivot service deliveries by group."""
        count_params = self.parse_count_request(request)
        pivot_params = self.parse_pivot_request(request)

        counts = self.get_count(count_params['by'], count_params['area_level'])
        df = pd.DataFrame(list(counts))

        # Convert all column values to string to simplify flatten the pivot table
        for col in pivot_params['columns']:
            df[col] = df[col].astype(str)

        # pivot
        df = pd.pivot_table(
            df,
            index=pivot_params['index'],
            columns=pivot_params['columns'],
            values=pivot_params['values'],
            fill_value=pivot_params['fill_value'],
            margins=pivot_params['margins'],
            margins_name=pivot_params['margins_name'],
            aggfunc=pivot_params['aggfunc'],
        )

        # flatten the pivot
        df.columns = df.columns.to_series().str.join('_')
        df.reset_index(inplace=True)

        return Response(df.to_dict('records'))

    def finalize_response(self, request, response, *args, **kwargs):
        """Setup filename for CSV response."""
        response = super(DeliveryPivotViewSet, self).finalize_response(
            request, response, *args, **kwargs)

        filename = '%s-%s.csv' % (slugify(self.get_view_name()), timezone.now().isoformat())
        if response.accepted_renderer.format == 'csv':
            response['content-disposition'] = 'attachment; filename=%s' % filename
        return response
