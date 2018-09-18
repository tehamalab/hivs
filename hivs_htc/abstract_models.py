from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class AbstractRegister(models.Model):
    date = models.DateField(_('date'))
    counselor_name = models.CharField(_('councelor name'), max_length=255)
    client_no = models.CharField(_('client number'), max_length=255)
    client_spouce_no = models.CharField(
        _('client spouce number'),
        max_length=255
    )
    attendance_type = models.CharField(_('attendance type'), max_length=255)
    gender = models.CharField(_('gender'), max_length=25)
    age = models.IntegerField(_('age'), validators=[MinValueValidator(0)])
    area = models.ForeignKey(
        'hivs_administrative.Area',
        related_name='htc_registers',
        verbose_name='area',
        help_text=_('administrative area where the client is comming from.'),
        on_delete=models.SET_NULL,
        null=True
    )
    martial_status = models.CharField(_('martial status'), max_length=25)
    pregnancy_status = models.CharField(_('pregnancy status'), max_length=25)
    referrer = models.CharField(_('referrer'), max_length=255, blank=True)
    councelling_type = models.CharField(_('councelling type'), max_length=255)
    agreed_to_test = models.BooleanField(_('agreed to test'), default=False)
    councelled_after_test = models.BooleanField(
        _('councelled after test'),
        default=False
    )
    test_result = models.CharField(_('test result'), max_length=25, blank=True)
    test_result_share = models.CharField(
        _('result sharing'),
        help_text=_('people who test results should be shared with'),
        max_length=25,
        blank=True
    )
    tb_tested = models.BooleanField(_('tested for TB'), default=False)
    tb_test_result = models.CharField(
        _('result for TB test'),
        max_length=25,
        blank=True
    )
    referred_to = models.CharField(
        _('referred to'),
        max_length=255,
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
    extras = JSONField(_('extras'), blank=True, default={})

    class Meta:
        abstract = True
        verbose_name = 'Register'
        verbose_name_plural = 'Register'

    def __str__(self):
        return self.client_no
