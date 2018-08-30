from django.contrib.gis import admin
from django.apps import apps
from django_mptt_admin.admin import DjangoMpttAdmin


Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AdministrativeAdmin(admin.OSMGeoAdmin, DjangoMpttAdmin):
    ordering = ['name']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'code', 'name', 'location_description_auto']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id', 'code']


class AreaAdmin(AdministrativeAdmin, admin.OSMGeoAdmin):
    raw_id_fields = ['parent']


class StreetAdmin(AdministrativeAdmin):
    raw_id_fields = ['area']


admin.site.register(Area, AreaAdmin)
admin.site.register(Street, StreetAdmin)
