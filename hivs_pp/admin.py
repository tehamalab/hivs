from django.contrib import admin
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter
from hivs_utils.admin import BaseAdmin
from .import_export import CategoryResource, ServiceResource, DeliveryResource
from .forms import DeliveryForm


Category = apps.get_registered_model('hivs_pp', 'Category')
Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')


class PPAdmin(BaseAdmin, ImportExportModelAdmin):
    readonly_fields = ['id', 'timestamp', 'last_modified']


@admin.register(Category)
class CategoryAdmin(PPAdmin):
    resource_class = CategoryResource
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['id']


@admin.register(Service)
class ServiceAdmin(PPAdmin):
    resource_class = ServiceResource
    list_display = ['id', 'name', 'category', 'is_confidential']
    list_display_links = ['id', 'name']
    list_select_related = ['category']
    list_filter = ['category', 'is_confidential']
    search_fields = ['id', 'name']
    ordering = ['id']


@admin.register(Delivery)
class DeliveryAdmin(PPAdmin):
    form = DeliveryForm
    resource_class = DeliveryResource
    list_display = ['id', 'date', 'gender', 'age', 'referral_made', 'referral_successful']
    list_display_links = ['id', 'date']
    list_select_related = ['gender']
    list_filter = ['date', ('date', DateRangeFilter), 'gender', 'services',
                   'referral_made', 'referral_successful', 'provider']
    filter_horizontal = ['services']
    raw_id_fields = ['client', 'provider', 'reviewer']
    search_fields = ['id', 'provider__username', 'services__name']
    ordering = ['-date']
