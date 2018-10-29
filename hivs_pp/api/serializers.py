from django.apps import apps
from rest_framework import serializers


Category = apps.get_registered_model('hivs_pp', 'Category')
Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'
