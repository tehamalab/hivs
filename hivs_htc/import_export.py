from django.apps import apps
from import_export import resources


Register = apps.get_model('hivs_htc', 'Register')


class RegisterResource(resources.ModelResource):

    class Meta:
        model = Register
