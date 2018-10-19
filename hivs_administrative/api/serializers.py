from django.apps import apps
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer


AreaType = apps.get_registered_model('hivs_administrative', 'AreaType')
Area = apps.get_registered_model('hivs_administrative', 'Area')
Street = apps.get_registered_model('hivs_administrative', 'Street')


class AreaSerializer(GeoFeatureModelSerializer):
    """GeoJSON Area serializer."""

    class Meta:
        model = Area
        fields = '__all__'
        geo_field = "geometry"


class StreetSerializer(GeoFeatureModelSerializer):
    """GeoJSON Area serializer."""

    class Meta:
        model = Street
        fields = '__all__'
        geo_field = "geometry"


class AreaTypeSerializer(ModelSerializer):
    """Area serializer."""

    class Meta:
        model = AreaType
        fields = '__all__'
