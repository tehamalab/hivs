from dateutil.relativedelta import relativedelta
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField, ArrayField


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
    area = models.ForeignKey(
        'hivs_administrative.Area',
        related_name='pp_deliveries',
        verbose_name='area',
        on_delete=models.SET_NULL,
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
    related_areas_ids = ArrayField(
        models.IntegerField(null=True, blank=True),
        verbose_name=_('related areas ids'),
        blank=True,
        null=True,
        editable=False
    )
    related_areas = ArrayField(
        models.CharField(max_length=255, blank=True),
        verbose_name=_('related areas'),
        blank=True,
        null=True,
        editable=False
    )

    class Meta:
        abstract = True
        verbose_name = _('Service Delived')
        verbose_name_plural = _('Services Delivered')

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        self.full_clean()

        # save related areas
        self.related_areas = list(
            self.area.get_ancestors(ascending=False, include_self=True).values_list('name', flat=True)
        )
        self.related_areas_ids = list(
            self.area.get_ancestors(ascending=False, include_self=True).values_list('id', flat=True)
        )

        super(AbstractDelivery, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """
        Get gender and age from clients profiles confidential instances.
        """
        errors = []

        if self.client:

            # try to populate gender from client's profile
            self.gender = self.client.gender or self.gender

            # try to populate area from client's profile if was not provided
            self.area = self.area or self.client.area

            # calculate age
            if self.client.birthdate:
                if self.date < self.client.birthdate:
                    errors.append(
                        ValidationError(_("Services date can not be before the client's birthdate."))
                    )
                self.age = relativedelta(self.date, self.client.birthdate).years

        # Ensure area , age and gender are provided.
        for attr in ['area', 'age', 'gender']:
            if not getattr(self, attr):
                errors.append(
                    ValidationError(_("Could not determine client's `{attr}`.".format(attr=attr)))
                )

        if errors:
            raise ValidationError(errors)

        super(AbstractDelivery, self).clean(*args, **kwargs)
