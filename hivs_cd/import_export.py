from django.apps import apps
from import_export import resources


Center = apps.get_model('hivs_cd', 'Center')
CondomDistribution = apps.get_model('hivs_cd', 'CondomDistribution')


class CenterResource(resources.ModelResource):

    class Meta:
        model = Center


class CondomDistributionResource(resources.ModelResource):

    class Meta:
        model = CondomDistribution
