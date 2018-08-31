from django.apps import apps
from import_export import resources


Category = apps.get_registered_model('hivs_pp', 'Category')
Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category


class ServiceResource(resources.ModelResource):

    class Meta:
        model = Service


class DeliveryResource(resources.ModelResource):

    class Meta:
        model = Delivery
