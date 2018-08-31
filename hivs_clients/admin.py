from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from .import_export import ProfileResource


Profile = apps.get_model('hivs_clients', 'Profile')


class ProfileAdmin(admin.OSMGeoAdmin, ImportExportModelAdmin):
    resource_class = ProfileResource


admin.site.register(Profile, ProfileAdmin)
