from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from hivs_utils.admin import BaseAdmin
from .import_export import CenterResource, CondomDistributionResource


Center = apps.get_model('hivs_cd', 'Center')
CondomDistribution = apps.get_model('hivs_cd', 'CondomDistribution')


class CenterAdmin(BaseAdmin, admin.OSMGeoAdmin, ImportExportModelAdmin):
    resource_class = CenterResource
    raw_id_fields = ['area', 'street']
    list_display = ['id', 'name', 'center_no']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id', 'center_no', 'area']


class CondomDistributionAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = CondomDistributionResource
    raw_id_fields = ['center']
    list_display = ['id', 'center', 'date']
    list_display_links = ['id', 'center']
    list_filter = ['date']
    search_fields = ['id', 'center__name']


admin.site.register(Center, CenterAdmin)
admin.site.register(CondomDistribution, CondomDistributionAdmin)
