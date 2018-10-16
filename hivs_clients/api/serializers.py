from django.apps import apps
from rest_framework import serializers


Profile = apps.get_model('hivs_clients', 'Profile')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
