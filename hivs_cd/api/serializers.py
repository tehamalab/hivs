from django.apps import apps
from rest_framework import serializers


Center = apps.get_registered_model('hivs_cd', 'Center')
Purpose = apps.get_registered_model('hivs_cd', 'Purpose')
CondomDistribution = apps.get_registered_model('hivs_cd', 'CondomDistribution')


class CenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Center
        fields = '__all__'


class PurposeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purpose
        fields = '__all__'


class CondomDistributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CondomDistribution
        fields = '__all__'
