from django.apps import apps
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from admin_numeric_filter.admin import NumericFilterModelAdmin, RangeNumericFilter
from hivs_utils.admin import BaseAdmin
from .import_export import (RegisterResource, ReferralCenterTypeResource,
                            ReferralCenterResource, ReferralResource)


Register = apps.get_model('hivs_htc', 'Register')
ReferralCenterType = apps.get_model('hivs_htc', 'ReferralCenterType')
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


@admin.register(ReferralCenterType)
class ReferralCenterTypeAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = ReferralCenterTypeResource
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Referral)
class ReferralAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = ReferralResource
    ordering = ['-date']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'date', 'register']
    list_display_links = ['id', 'date', 'register']
    list_select_related = ['register']
    list_filter = ['date', 'referrer_center__center_type']
    search_fields = ['id', 'register__client_no']


class ReferralInline(admin.StackedInline):
    model = Referral
    extra = 1


@admin.register(Register)
class RegisterAdmin(BaseAdmin, NumericFilterModelAdmin, ImportExportModelAdmin):
    resource_class = RegisterResource
    inlines = [ReferralInline]
    ordering = ['-date']
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'date', 'client_no', 'gender', 'marital_status',
                    'agreed_to_test', 'tb_screened']
    list_display_links = ['id', 'date', 'client_no']
    list_select_related = ['gender', 'marital_status']
    list_filter = ['date', 'gender', ('age', RangeNumericFilter),
                   'attendance_type', 'counselling_type',
                   'marital_status', 'pregnancy_status', 'agreed_to_test',
                   'hiv_test_result', 'tb_screened', 'tb_screening_result']
    search_fields = ['id', 'client_no', 'area']
