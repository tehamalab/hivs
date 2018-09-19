from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from .import_export import CenterResource, CondomDistributionResource


Center = apps.get_model('hivs_cd', 'Center')
CondomDistribution = apps.get_model('hivs_cd', 'CondomDistribution')


class CenterAdmin(admin.OSMGeoAdmin, ImportExportModelAdmin):
    resource_class = CenterResource


class CondomDistributionAdmin(ImportExportModelAdmin):
    resource_class = CondomDistributionResource


admin.site.register(Center, CenterAdmin)
admin.site.register(CondomDistribution, CondomDistributionAdmin)
