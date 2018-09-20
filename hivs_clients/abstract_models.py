from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class AbstractProfile(models.Model):
    registration_id = models.CharField(
        _('registration number'),
        max_length=255,
        blank=True
    )
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    middle_name = models.CharField(_('middle name'), max_length=255, blank=True)
    gender = models.ForeignKey(
        'hivs_utils.Gender',
        related_name='clients_profiles',
        verbose_name='gender',
        on_delete=models.SET_NULL,
        null=True
    )
    martial_status = models.ForeignKey(
        'hivs_utils.MartialStatus',
        related_name='clients_profiles',
        verbose_name='martial status',
        on_delete=models.SET_NULL,
        null=True
    )
    birthdate = models.DateField(_('birthdate'), blank=True, null=True)
    phone = PhoneNumberField(_('phone number'), blank=True)
    other_phones = ArrayField(
        PhoneNumberField(),
        blank=True,
        default=[],
        verbose_name=_('other phones')
    )
    email = models.EmailField(_('email'), blank=True)
    education_level = models.CharField(_('education level'), max_length=255, blank=True)
    occupation = models.CharField(_('occupation'), max_length=255, blank=True)
    area = models.ForeignKey(
        'hivs_administrative.Area',
        related_name='clients_profiles',
        verbose_name='administrative area',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    street = models.ForeignKey(
        'hivs_administrative.Street',
        related_name='clients_profiles',
        verbose_name='street',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    geolocation = models.PointField(
        _('geolocation'),
        blank=True,
        null=True,
        geography=True
    )
    timestamp = models.DateTimeField('Created at', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('Last modified'),
        auto_now=True,
        null=True,
        blank=True
    )
    extras = JSONField(_('extras'), blank=True, default=dict)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        abstract = True

    def __str__(self):
        return ' '.join(filter(None, [self.registration_id, self.first_name, self.last_name]))
