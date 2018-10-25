from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from hivs_utils.admin import BaseAdmin
from .import_export import CenterResource, PurposeResource, CondomDistributionResource


Center = apps.get_model('hivs_cd', 'Center')
Purpose = apps.get_model('hivs_cd', 'Purpose')
CondomDistribution = apps.get_model('hivs_cd', 'CondomDistribution')


@admin.register(Center)
class CenterAdmin(BaseAdmin, admin.OSMGeoAdmin, ImportExportModelAdmin):
    resource_class = CenterResource
    raw_id_fields = ['area', 'street']
    list_display = ['id', 'name', 'center_no']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id', 'center_no', 'area']


@admin.register(Purpose)
class PurposeAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = PurposeResource
    list_display = ['id', 'name', 'code']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id']


@admin.register(CondomDistribution)
class CondomDistributionAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = CondomDistributionResource
    raw_id_fields = ['center']
    list_display = ['id', 'center', 'condoms_male_count', 'condoms_female_count', 'date']
    list_display_links = ['id', 'center']
    list_filter = ['date', 'gender', 'attendance_type', 'purpose']
    search_fields = ['id', 'center__name']
