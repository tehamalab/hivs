from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from hivs_utils.admin import BaseAdmin
from .import_export import (RegisterResource, ReferralCenterResource,
                            ReferralResource)


Register = apps.get_model('hivs_htc', 'Register')
ReferralCenter = apps.get_model('hivs_htc', 'ReferralCenter')
Referral = apps.get_model('hivs_htc', 'Referral')


@admin.register(ReferralCenter)
class ReferralCenterAdmin(BaseAdmin, admin.OSMGeoAdmin,
                          ImportExportModelAdmin):
    resource_class = ReferralCenterResource
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'description']


@admin.register(Referral)
class ReferralAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = ReferralResource
    ordering = ['-date']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'date', 'register']
    list_display_links = ['id', 'date', 'register']
    list_select_related = ['register']
    list_filter = ['date', 'referral_center__center_type',
                   'referrer_center__center_type']
    search_fields = ['id', 'register__client_no']


class ReferralInline(admin.StackedInline):
    model = Referral
    extra = 1


@admin.register(Register)
class RegisterAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = RegisterResource
    inlines = [ReferralInline]
    ordering = ['-date']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'date', 'client_no']
    list_display_links = ['id', 'date', 'client_no']
    list_filter = ['date', 'gender', 'attendance_type', 'martial_status',
                   'pregnancy_status', 'agreed_to_test', 'tb_tested']
    search_fields = ['id', 'client_no', 'area']
