from django.contrib.gis import admin
from django.apps import apps
from django_mptt_admin.admin import DjangoMpttAdmin
from import_export.admin import ImportExportModelAdmin
from .import_export import AreaResource, StreetResource


Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AdministrativeAdmin(admin.OSMGeoAdmin, ImportExportModelAdmin):
    ordering = ['name']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'code', 'name', 'location_description_auto']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id', 'code']


class AreaAdmin(AdministrativeAdmin, DjangoMpttAdmin):
    resource_class = AreaResource
    raw_id_fields = ['parent']


class StreetAdmin(AdministrativeAdmin):
    resource_class = StreetResource
    raw_id_fields = ['area']


admin.site.register(Area, AreaAdmin)
admin.site.register(Street, StreetAdmin)
