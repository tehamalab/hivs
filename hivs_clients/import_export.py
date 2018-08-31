from django.apps import apps
from import_export import resources


Profile = apps.get_model('hivs_clients', 'Profile')


class ProfileResource(resources.ModelResource):

    class Meta:
        model = Profile
