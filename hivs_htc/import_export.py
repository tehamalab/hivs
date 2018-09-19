from django.apps import apps
from import_export import resources


Register = apps.get_model('hivs_htc', 'Register')
ReferralCenter = apps.get_model('hivs_htc', 'ReferralCenter')
Referral = apps.get_model('hivs_htc', 'Referral')


class RegisterResource(resources.ModelResource):

    class Meta:
        model = Register


class ReferralCenterResource(resources.ModelResource):

    class Meta:
        model = ReferralCenter


class ReferralResource(resources.ModelResource):

    class Meta:
        model = Referral
