from django.apps import apps
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


Service = apps.get_registered_model('hivs_pp', 'Service')
Delivery = apps.get_registered_model('hivs_pp', 'Delivery')


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = '__all__'

    def clean(self):
        """
        Ensure instances with confidential services are not linked with clients profiles.
        """
        confidential = False
        for service in self.cleaned_data.get('services'):
            if service.is_confidential:
                confidential = True
                break
        if confidential:
            if self.cleaned_data.get('client'):
                raise ValidationError(_('Services delivered including confidential services '
                                        'can not be linked with clients profiles.'))
        return self.cleaned_data
