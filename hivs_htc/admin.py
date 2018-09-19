from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from .import_export import (RegisterResource, ReferralCenterResource,
                            ReferralResource)


Register = apps.get_model('hivs_htc', 'Register')
ReferralCenter = apps.get_model('hivs_htc', 'ReferralCenter')
Referral = apps.get_model('hivs_htc', 'Referral')


class ReferralCenterAdmin(admin.OSMGeoAdmin, ImportExportModelAdmin):
    resource_class = ReferralCenterResource,


class ReferralAdmin(ImportExportModelAdmin):
    resource_class = ReferralResource


class ReferralInline(admin.StackedInline):
    model = Referral
    extra = 1


class RegisterAdmin(ImportExportModelAdmin):
    resource_class = RegisterResource
    inlines = [ReferralInline]


admin.site.register(Register, RegisterAdmin)
admin.site.register(ReferralCenter, ReferralCenterAdmin)
admin.site.register(Referral, ReferralAdmin)
