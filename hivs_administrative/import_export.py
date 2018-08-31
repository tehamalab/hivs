from django.apps import apps
from import_export import resources


Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AreaResource(resources.ModelResource):

    class Meta:
        model = Area


class StreetResource(resources.ModelResource):

    class Meta:
        model = Street
