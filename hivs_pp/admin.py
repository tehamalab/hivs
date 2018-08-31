from django.contrib import admin
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from .import_export import CategoryResource, ServiceResource, DeliveryResource


Category = apps.get_registered_model('hivs_pp', 'Category')
Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')


class PPAdmin(ImportExportModelAdmin):
    readonly_fields = ['id', 'timestamp', 'last_modified']


class CategoryAdmin(PPAdmin):
    resource_class = CategoryResource
    search_fields = ['id', 'name']


class ServiceAdmin(PPAdmin):
    resource_class = ServiceResource
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['id', 'name']


class DeliveryAdmin(PPAdmin):
    resource_class = DeliveryResource
    list_display = ['id', 'client']
    list_display_links = ['id', 'client']
    list_filter = ['provider', 'date']
    filter_horizontal = ['services']
    raw_id_fields = ['client', 'provider', 'reviewer']
    search_fields = ['id', 'provider__username', 'services__name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Delivery, DeliveryAdmin)
