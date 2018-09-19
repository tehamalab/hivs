from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HivsUtilsConfig(AppConfig):
    name = 'hivs_utils'
    verbose_name = _('Shared modules')
