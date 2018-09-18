from django.apps import apps
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .import_export import RegisterResource


Register = apps.get_model('hivs_htc', 'Register')


class RegisterAdmin(ImportExportModelAdmin):
    resource_class = RegisterResource


admin.site.register(Register, RegisterAdmin)
