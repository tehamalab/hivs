from dateutil.relativedelta import relativedelta
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
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
    location = models.CharField(_('location description'), max_length=255, blank=True)
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


class AbstractPurpose(models.Model):
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
        verbose_name = _('Condom Distribution Purpose')
        verbose_name_plural = _('Condom Distribution Purposes')

    def __str__(self):
        return self.name


class AbstractCondomDistribution(models.Model):
    date = models.DateField(_('date'))
    client = models.ForeignKey(
        'hivs_clients.Profile',
        related_name='condom_distributions',
        verbose_name=_('client profile'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    gender = models.ForeignKey(
        'hivs_utils.Gender',
        related_name='condom_distributions',
        verbose_name='client gender',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    age = models.IntegerField(
        _('client age'),
        validators=[MinValueValidator(0)],
        blank=True,
    )
    attendance_type = models.ForeignKey(
        'hivs_utils.AttendanceType',
        related_name='condom_distributions',
        verbose_name='attendance type',
        on_delete=models.SET_NULL,
        null=True
    )
    condoms_male_count = models.IntegerField(
        _('No. of male condoms provided'),
        help_text=_('No. of male condoms delivered'),
        validators=[MinValueValidator(0)],
        default=0,
        blank=True
    )
    condoms_female_count = models.IntegerField(
        _('No. of female condoms provided'),
        help_text=_('No. of male condoms delivered'),
        validators=[MinValueValidator(0)],
        default=0,
        blank=True
    )
    purpose = models.ForeignKey(
        'hivs_cd.Purpose',
        related_name='condom_distributions',
        verbose_name='purpose',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    education_delivered = models.BooleanField(
        _('Education was delivered'),
        default=False
    )
    education_topics = models.ManyToManyField(
        'hivs_utils.Topic',
        related_name='condom_distributions',
        verbose_name=_('Education topics delivered'),
        blank=True
    )
    referral_made = models.BooleanField(_('referral was given'), default=False)
    referral_type = models.ForeignKey(
        'hivs_htc.ReferralCenterType',
        related_name='condom_distriputions',
        verbose_name='type of referral given',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    distributor_name = models.CharField(_('distributor name'), max_length=255)
    distributor_contact = models.CharField(_('distributor contact'), max_length=255, blank=True)
    center = models.ForeignKey(
        'hivs_cd.Center',
        related_name='condom_distributions',
        verbose_name='distribution center',
        on_delete=models.SET_NULL,
        null=True
    )
    remarks = models.TextField(_('remarks'), blank=True)
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

    def save(self, *args, **kwargs):
        self.full_clean()
        super(AbstractCondomDistribution, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """
        Get gender and age from clients profile info.
        """
        errors = []

        if self.client:

            # try to populate gender from client's profile
            self.gender = self.client.gender or self.gender

            # calculate age
            if self.client.birthdate:
                if self.date < self.client.birthdate:
                    errors.append(
                        ValidationError(_("Services date can not be before the client's birthdate."))
                    )
                self.age = relativedelta(self.date, self.client.birthdate).years

        # Ensure area , age and gender are provided.
        for attr in ['age', 'gender']:
            if not getattr(self, attr):
                errors.append(
                    ValidationError(_("Could not determine client's `{attr}`.".format(attr=attr)))
                )

        if errors:
            raise ValidationError(errors)

        super(AbstractCondomDistribution, self).clean(*args, **kwargs)
