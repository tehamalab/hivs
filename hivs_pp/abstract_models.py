from dateutil.relativedelta import relativedelta
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
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
    is_confidential = models.BooleanField(
        _('is confidential'),
        help_text=_('select if this service delivery information should not be linked '
                    'with clients profiles'),
        default=False
    )
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
        help_text=_('Do not fill this field is some of the provided services are confidential.'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    gender = models.ForeignKey(
        'hivs_utils.Gender',
        related_name='pp_deliveries',
        verbose_name='client gender',
        help_text=_("If client profile is set this can be overwritten based on the client's profile."),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    age = models.IntegerField(
        _('client age'),
        help_text=_("If client profile is set this can be overwritten based on the client's birthdate."),
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    services = models.ManyToManyField(
        'hivs_pp.Service',
        related_name='deliveries',
        verbose_name=_('services provided')
    )
    referral_made = models.BooleanField(_('referral was issued'), default=False)
    referral_successful = models.BooleanField(_('referral was succesful'), default=False)
    remarks = models.TextField(_('remarks'), blank=True)
    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pp_delivery_providers',
        verbose_name=_('service provider'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
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
        verbose_name = _('Service Delived')
        verbose_name_plural = _('Services Delivered')

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(AbstractDelivery, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """
        Get gender and age from clients profiles confidential instances.
        """
        if self.client:
            errors = []
            self.gender = self.client.gender or self.gender
            if not self.gender:
                errors.append(
                    ValidationError(_("Could not find gender for the client."))
                )
            # calculate age
            if self.client.birthdate:
                if self.date < self.client.birthdate:
                    errors.append(
                        ValidationError(_("Services date can not be before the client's birthdate."))
                    )
                self.age = relativedelta(self.date, self.client.birthdate).years

            if errors:
                raise ValidationError(errors)

        super(AbstractDelivery, self).clean(*args, **kwargs)
