from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from phonenumber_field.modelfields import PhoneNumberField


class AbstractCenter(models.Model):
    name = models.CharField(_('name'), max_length=255)
    center_no = models.CharField(
        _('center number'),
        max_length=255,
        unique=True
    )
    area = models.ForeignKey(
        'hivs_administrative.Area',
        related_name='cd_centers',
        verbose_name='area',
        help_text=_('administrative area where the center is located'),
        on_delete=models.SET_NULL,
        null=True
    )
    street = models.ForeignKey(
        'hivs_administrative.Street',
        related_name='cd_centers',
        verbose_name='street',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    location = models.CharField(_('location description'), max_length=255)
    geolocation = models.PointField(
        _('geolocation'),
        blank=True,
        null=True,
        geography=True
    )
    phone = PhoneNumberField(_('phone number'), blank=True)
    email = models.EmailField(_('email'), blank=True)
    timestamp = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )
    extras = JSONField(_('extras'), blank=True, default=dict)

    class Meta:
        abstract = True
        verbose_name = 'Condom Distribution Center'
        verbose_name_plural = 'Condom Distribution Centers'

    def __str__(self):
        return self.name


class AbstractCondomDistribution(models.Model):
    date = models.DateField(_('date'))
    center = models.ForeignKey(
        'hivs_cd.Center',
        related_name='cd_condom_distributions',
        verbose_name='distribution center',
        on_delete=models.SET_NULL,
        null=True
    )
    distributor_name = models.CharField(_('distributor name'), max_length=255)
    gender = models.CharField(_('gender'), max_length=25)
    age = models.IntegerField(_('age'), validators=[MinValueValidator(0)])
    attendance_type = models.ForeignKey(
        'hivs_utils.AttendanceType',
        related_name='condom_distributions',
        verbose_name='attendance type',
        on_delete=models.SET_NULL,
        null=True
    )
    hiv_education_delivered = models.BooleanField(
        _('HIV education was delivered'),
        default=False
    )
    hiv_education_topics = models.CharField(
        _('HIV education topics delivered'),
        max_length=255,
        blank=True
    )
    condoms_male_count = models.IntegerField(
        _('male condoms'),
        help_text=_('No. of male condoms delivered'),
        validators=[MinValueValidator(0)],
        default=0
    )
    condoms_female_count = models.IntegerField(
        _('female condoms'),
        help_text=_('No. of male condoms delivered'),
        validators=[MinValueValidator(0)],
        default=0
    )
    referral_given = models.BooleanField(_('referral was given'), default=False)
    referral_given_type = models.CharField(
        _('referred to'),
        max_length=255,
        blank=True
    )
    timestamp = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )
    extras = JSONField(_('extras'), blank=True, default=dict)

    class Meta:
        abstract = True
        verbose_name = 'Condom Distribution'
        verbose_name_plural = 'Condoms Distributions'

    def __str__(self):
        return '{}: {}'.format(self.center.name, self.date)
