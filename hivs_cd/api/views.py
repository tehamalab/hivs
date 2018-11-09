import pandas as pd
from django.apps import apps
from django.db.models import Count, Sum
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from rest_framework import status
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.exceptions import APIException, MethodNotAllowed
from rest_framework.decorators import action
from rest_framework_csv.renderers import CSVStreamingRenderer
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
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVStreamingRenderer, )
    ordering = ['-date']
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
    count_by = [
        'date',
        'gender',
        'gender__name',
        'age',
        'attendance_type',
        'attendance_type__name',
        'purpose',
        'purpose__name',
        'education_delivered',
        'education_topics',
        'education_topics__name',
        'referral_made',
        'referral_type',
        'referral_type__name',
        'center',
        'center__name',
        'center__area',
        'center__area__name',
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

        return {'by': by}

    parse_sum_request = parse_count_request

    def get_count(self, by):
        """Count condom distributions per group."""

        # ordering causes duplicate entries if not part of grouping. See
        # https://docs.djangoproject.com/en/dev/topics/db/aggregation/#interaction-with-default-ordering-or-order-by
        for i in self.ordering:
            if i not in by:
                self.ordering.remove(i)

        queryset = self.filter_queryset(self.get_queryset())
        return queryset.values(*by).annotate(count=Count('*'))[:1000]

    def get_sum(self, by):
        """Sum condoms distributed per group."""

        # ordering causes duplicate entries if not part of grouping. See
        # https://docs.djangoproject.com/en/dev/topics/db/aggregation/#interaction-with-default-ordering-or-order-by
        for i in self.ordering:
            if i not in by:
                self.ordering.remove(i)

        queryset = self.filter_queryset(self.get_queryset())
        return queryset.values(*by).annotate(
            condoms_count=(Sum('condoms_male_count') + Sum('condoms_female_count')),
            condoms_male_count=Sum('condoms_male_count'),
            condoms_female_count=Sum('condoms_female_count')
        )[:1000]

    @action(detail=False, methods=['get'])
    def total(self, request, *args, **kwargs):
        """Total condom distribution."""
        queryset = self.filter_queryset(self.get_queryset())
        data = queryset.aggregate(
            count=Count('*'),
            condoms_male_count=Sum('condoms_male_count'),
            condoms_female_count=Sum('condoms_female_count'),
            condoms_count=(Sum('condoms_male_count') + Sum('condoms_female_count'))
        )
        return Response(data)

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        """Count of condom distributions per group."""
        params = self.parse_count_request(request)
        return Response(list(self.get_count(params['by'])))

    @action(detail=False, methods=['get'])
    def sum(self, request, *args, **kwargs):
        """Sum of condoms distributed per group."""
        params = self.parse_sum_request(request)
        return Response(list(self.get_sum(params['by'])))

    def finalize_response(self, request, response, *args, **kwargs):
        """Setup filename for CSV response."""
        response = super(CondomDistributionViewSet, self).finalize_response(
            request, response, *args, **kwargs)

        if response.accepted_renderer.format == 'csv':
            filename = request.query_params.get('filename') \
                or '%s-%s.csv' % (slugify(self.get_view_name()), timezone.now().isoformat())
            response['content-disposition'] = 'attachment; filename=%s' % filename

        return response


class CondomDistributionPivotViewSet(CondomDistributionViewSet):
    """
    Condom Distribution Pivot Table.
    """

    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVStreamingRenderer, )
    rows_fields = ['date', 'gender', 'gender__name', 'age', 'center', 'center__name',
                   'attendance_type', 'attendance_type__name', 'purpose',
                   'purpose__name', 'referral_made', 'referral_type', 'referral_type__name']
    columns_fields = rows_fields
    values_fields = ['condoms_male_count', 'condoms_female_count', 'condoms_count', 'count']
    aggregations = ['mean', 'sum', 'count']

    pivots_columns = {
        'referrals': {
            'count:False': 'unsuccessful_referrals',
            'count:True': 'successful_referrals',
            'count:total': 'referrals_made'
        },
        'gender': {
            ':Male': ':male_clients',
            ':Female': ':female_clients',
            'count:total': 'total'
        },
        'age': {
            'count:total': 'total',
            'count:': 'age_',
        },
        'age_range': {
            'count:total': 'total',
            'count:nan': 'age_other',
            'count:': 'age_',
            'age:Male|Male': ':male_clients',
            'age:Female|Female': ':female_clients',
        },
    }

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

        agg = request.query_params.get('aggregation', 'sum')
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

    def pivot(self, request, agg, *args, **kwargs):
        """Count and pivot service deliveries by group."""
        count_params = self.parse_count_request(request)
        pivot_params = self.parse_pivot_request(request)
        pivot_type = request.query_params.get('pivot_type')

        if agg == 'count':
            counts = self.get_count(count_params['by'])
        else:
            counts = self.get_sum(count_params['by'])

        # create datafrane
        df = pd.DataFrame(list(counts))

        if df.empty:
            return Response(df.to_dict('records'))

        if pivot_type == 'age_range':
            if 'age' not in df:
                raise APIException(_('`age` values not in dataset.'), status.HTTP_400_BAD_REQUEST)

            bins = request.query_params.get('range_limits', '').split(',')
            if not bins:
                raise APIException(_('Missing `range_limits`.'), status.HTTP_400_BAD_REQUEST)
            elif len(bins) < 2:
                raise APIException(_('`range_limits` must contain at least 2 values.'),
                                   status.HTTP_400_BAD_REQUEST)
            try:
                bins = [int(i) for i in bins]
            except ValueError:
                raise APIException(_('Invalid `range_limits`.'), status.HTTP_400_BAD_REQUEST)

            labels = request.query_params.get('range_labels', '').split(',')
            if labels and len(labels) != (len(bins) - 1):
                raise APIException(_('Invalid `range_labels`.'), status.HTTP_400_BAD_REQUEST)
            elif not labels:
                for i, v in enumerate(bins):
                    if i is not 0:
                        labels.append('{}-{}'.format(bins[i-1], v))

            df = df.assign(age_range=pd.cut(df.age, bins=bins, labels=labels, right=False))

        # Convert all column values to string to simplify flattening of the pivot table
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
        df.columns = df.columns.to_series().str.join(':')
        df.reset_index(inplace=True)

        # rename some columns
        if pivot_type and pivot_type in self.pivots_columns:
            for old, new in self.pivots_columns[pivot_type].items():
                df.columns = df.columns.str.replace(old, new)

        return Response(df.to_dict('records'))

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        return self.pivot(request, 'count', *args, **kwargs)

    @action(detail=False, methods=['get'])
    def sum(self, request, *args, **kwargs):
        return self.pivot(request, 'sum', *args, **kwargs)
