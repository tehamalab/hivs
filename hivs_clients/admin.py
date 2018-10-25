from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from hivs_utils.admin import BaseAdmin
from .import_export import ProfileResource


Profile = apps.get_model('hivs_clients', 'Profile')


@admin.register(Profile)
class ProfileAdmin(BaseAdmin, admin.OSMGeoAdmin, ImportExportModelAdmin):
    resource_class = ProfileResource
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'first_name', 'last_name', 'registration_id']
    list_display_links = ['id', 'first_name', 'last_name']
    list_filter = ['gender', 'martial_status', 'timestamp']
    search_fields = ['id', 'first_name', 'last_name', 'registration_id',
                     'area__name', 'street__name']
