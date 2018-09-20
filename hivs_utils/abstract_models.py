from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractChoice(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    code = models.CharField(_('code'), max_length=25, blank=True)
    timestamp = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
