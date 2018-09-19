from django.apps import apps
from import_export import resources, fields, widgets


Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')
AreaType = apps.get_registered_model('hivs_administrative', 'AreaType')


class AreaTypeResource(resources.ModelResource):

    class Meta:
        model = AreaType


class AreaResource(resources.ModelResource):
    parent = fields.Field(
        attribute='parent',
        widget=widgets.ForeignKeyWidget(Area)
    )

    class Meta:
        model = Area


class StreetResource(resources.ModelResource):

    class Meta:
        model = Street
