from django.apps import apps
from import_export import resources


Center = apps.get_model('hivs_cd', 'Center')
Purpose = apps.get_model('hivs_cd', 'Purpose')
CondomDistribution = apps.get_model('hivs_cd', 'CondomDistribution')


class CenterResource(resources.ModelResource):

    class Meta:
        model = Center


class PurposeResource(resources.ModelResource):

    class Meta:
        model = Purpose


class CondomDistributionResource(resources.ModelResource):

    class Meta:
        model = CondomDistribution
