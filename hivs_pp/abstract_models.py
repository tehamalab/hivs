from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class AbstractCategory(models.Model):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    timestamp = models.DateTimeField('timestamp', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class AbstractService(models.Model):
    category = models.ForeignKey(
        'hivs_pp.Category',
        verbose_name=_('category'),
        related_name='services',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    timestamp = models.DateTimeField('timestamp', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.name


class AbstractDelivery(models.Model):
    date = models.DateField(_('date'))
    time = models.TimeField(_('time'), blank=True, null=True)
    client = models.ForeignKey(
        'hivs_clients.Profile',
        related_name='pp_deliveries',
        verbose_name=_('client profile'),
        on_delete=models.SET_NULL,
        null=True
    )
    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pp_delivery_providers',
        verbose_name=_('service provider'),
        on_delete=models.SET_NULL,
        null=True
    )
    services = models.ManyToManyField(
        'hivs_pp.Service',
        related_name='deliveries',
        verbose_name=_('services delivered')
    )
    remarks = models.TextField(_('remarks'), blank=True)
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pp_delivery_reviewers',
        verbose_name=_('reviewer'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    review_remarks = models.TextField(_('review remarks'), blank=True)
    review_date = models.DateField(_('review date'), blank=True, null=True)
    review_time = models.TimeField(_('review time'), blank=True, null=True)
    extras = JSONField(_('extras'), blank=True, default=dict)
    timestamp = models.DateTimeField('timestamp', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Service Delivery')
        verbose_name_plural = _('Services Deliveries')

    def __str__(self):
        return self.date
