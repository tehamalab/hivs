from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from hivs_utils.datetime import today


class AbstractProfile(models.Model):
    registration_id = models.CharField(
        _('registration number'),
        max_length=255,
        blank=True
    )
    acquisition_date = models.DateField(_('acquisition date'), default=today)
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
    marital_status = models.ForeignKey(
        'hivs_utils.MaritalStatus',
        related_name='clients_profiles',
        verbose_name='marital status',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    birthdate = models.DateField(_('birthdate'), blank=True, null=True)
    phone = PhoneNumberField(_('phone number'), blank=True)
    other_phones = ArrayField(
        PhoneNumberField(),
        blank=True,
        default=list,
        verbose_name=_('other phones')
    )
    email = models.EmailField(_('email'), blank=True)
    education_level = models.ForeignKey(
        'hivs_utils.EducationLevel',
        related_name='clients_profiles',
        verbose_name='education level',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    occupation = models.ForeignKey(
        'hivs_utils.Occupation',
        related_name='clients_profiles',
        verbose_name='occupation',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
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
