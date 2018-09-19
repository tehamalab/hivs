from django.contrib.gis import admin
from django.apps import apps
from django_mptt_admin.admin import DjangoMpttAdmin
from import_export.admin import ImportExportModelAdmin
from hivs_utils.admin import BaseAdmin
from .import_export import AreaTypeResource, AreaResource, StreetResource


AreaType = apps.get_registered_model('hivs_administrative', 'AreaType')
Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AdministrativeAdmin(BaseAdmin, admin.OSMGeoAdmin, ImportExportModelAdmin):
    ordering = ['name']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'name', 'location_description_auto']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id', 'code']


@admin.register(AreaType)
class AreaTypeAdmin(AdministrativeAdmin):
    resource_class = AreaTypeResource
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(Area)
class AreaAdmin(AdministrativeAdmin, DjangoMpttAdmin):
    resource_class = AreaResource
    list_display = ['id', 'name', 'location_description_auto', 'area_type']
    list_select_related = ['area_type']
    list_filter = ['area_type']
    raw_id_fields = ['parent']


@admin.register(Street)
class StreetAdmin(AdministrativeAdmin):
    resource_class = StreetResource
    raw_id_fields = ['area']
