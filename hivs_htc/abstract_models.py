from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from phonenumber_field.modelfields import PhoneNumberField


class AbstractRegister(models.Model):
    date = models.DateField(_('date'))
    counselor_name = models.CharField(_('councelor name'), max_length=255)
    client_no = models.CharField(_('client number'), max_length=255)
    client_spouce_no = models.CharField(
        _('client spouce number'),
        max_length=255,
        blank=True,
    )
    attendance_type = models.ForeignKey(
        'hivs_utils.AttendanceType',
        related_name='htc_registers',
        verbose_name='attendance type',
        on_delete=models.SET_NULL,
        null=True
    )
    gender = models.ForeignKey(
        'hivs_utils.Gender',
        related_name='htc_registers',
        verbose_name='gender',
        on_delete=models.SET_NULL,
        null=True
    )
    age = models.IntegerField(_('age'), validators=[MinValueValidator(0)])
    area = models.ForeignKey(
        'hivs_administrative.Area',
        related_name='htc_registers',
        verbose_name='area',
        help_text=_('administrative area where the client is comming from.'),
        on_delete=models.SET_NULL,
        null=True
    )
    martial_status = models.ForeignKey(
        'hivs_utils.MartialStatus',
        related_name='htc_registers',
        verbose_name='martial status',
        on_delete=models.SET_NULL,
        null=True
    )
    pregnancy_status = models.ForeignKey(
        'hivs_utils.PregnancyStatus',
        related_name='htc_registers',
        verbose_name='pregnancy status',
        on_delete=models.SET_NULL,
        null=True
    )
    referrer_type = models.ForeignKey(
        'hivs_htc.ReferralCenterType',
        related_name='htc_referrer_registers',
        verbose_name=_('referred from'),
        help_text=_('Where the client is coming from'),
        on_delete=models.SET_NULL,
        null=True
    )
    counselling_type = models.ForeignKey(
        'hivs_utils.CounsellingType',
        related_name='htc_registers',
        verbose_name='counselling type',
        on_delete=models.SET_NULL,
        null=True
    )
    agreed_to_test = models.BooleanField(_('agreed to test'), default=False)
    counselled_after_test = models.BooleanField(
        _('counselled after test'),
        default=False
    )
    hiv_test_result = models.ForeignKey(
        'hivs_utils.HIVStatus',
        related_name='htc_register_results',
        verbose_name='HIV test result',
        on_delete=models.SET_NULL,
        null=True
    )
    test_result_share = models.ForeignKey(
        'hivs_utils.ResultSharingChoice',
        related_name='htc_register_results',
        verbose_name='result sharing',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tb_screened = models.BooleanField(_('screened for TB'), default=False)
    tb_screening_result = models.ForeignKey(
        'hivs_utils.TBStatus',
        related_name='htc_register_screening',
        verbose_name='TB screening result',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    received_condoms = models.BooleanField(_('received condom(s)'), default=False)
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
        verbose_name = _('HTC Register')
        verbose_name_plural = _('HTC Registers')

    def __str__(self):
        return self.client_no


class AbstractReferralCenterType(models.Model):
    name = models.CharField(_('center type'), max_length=255, unique=True)
    code = models.CharField(_('code'), max_length=25, blank=True)
    description = models.TextField(_('description'), blank=True)
    timestamp = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Referral Type')
        verbose_name_plural = _('Referral Types')

    def __str__(self):
        return self.name


class AbstractReferralCenter(models.Model):
    center_type = models.ForeignKey(
        'hivs_htc.ReferralCenterType',
        related_name='htc_referral_centers',
        verbose_name='center type',
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(_('name'), max_length=255)
    phone = PhoneNumberField(_('phone number'), blank=True)
    email = models.EmailField(_('email'), blank=True)
    address = models.TextField(_('address'), blank=True)
    area = models.ForeignKey(
        'hivs_administrative.Area',
        related_name='referral_centers',
        verbose_name='administrative area',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    street = models.ForeignKey(
        'hivs_administrative.Street',
        related_name='referral_centers',
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
    extras = JSONField(_('extras'), blank=True, default=dict)
    timestamp = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Referral Center')
        verbose_name_plural = _('Referral Centers')

    def __str__(self):
        return self.name


class AbstractReferral(models.Model):
    register = models.ForeignKey(
        'hivs_htc.Register',
        related_name='referrals',
        verbose_name=_('Client registered as'),
        on_delete=models.SET_NULL,
        null=True
    )
    date = models.DateField(_('date'))
    referral_center = models.ForeignKey(
        'hivs_htc.ReferralCenter',
        related_name='htc_referrals',
        verbose_name=_('referred to'),
        on_delete=models.SET_NULL,
        null=True
    )
    reason = models.CharField(_('reason'), max_length=255)
    services_given = models.TextField(_('services given'))
    unique_info = models.TextField(
        _('unique information'),
        help_text=_('Example; allergy'),
        blank=True
    )
    referrer_center = models.ForeignKey(
        'hivs_htc.ReferralCenter',
        related_name='htc_referrers',
        verbose_name=_('referred from'),
        help_text=_('center that issues the referral'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    issuer_name = models.CharField(
        _('issuer name'),
        help_text=_('name of a person who issued the referral'),
        max_length=255,
        blank=True
    )
    issuer_designation = models.CharField(
        _('issuer designation'),
        help_text=_('designation of a person who issued the referral'),
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

    class Meta:
        abstract = True
        verbose_name = _('Referral')
        verbose_name_plural = _('Referrals')

    def __str__(self):
        return self.client_no
