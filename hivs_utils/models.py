from django.db import models
from django.utils.translation import ugettext_lazy as _


class Gender(models.Model):
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
        verbose_name = 'Gender'
        verbose_name_plural = 'Gender'

    def __str__(self):
        return self.name


class MartialStatus(models.Model):
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
        verbose_name = 'Martial status'
        verbose_name_plural = 'Martial status'

    def __str__(self):
        return self.name


class PregnancyStatus(models.Model):
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
        verbose_name = 'Pregnancy status'
        verbose_name_plural = 'Pregnancy status'

    def __str__(self):
        return self.name


class AttendanceType(models.Model):
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
        verbose_name = 'Attendance type'
        verbose_name_plural = 'Attendance types'

    def __str__(self):
        return self.name


class HIVStatus(models.Model):
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
        verbose_name = 'HIV Status'
        verbose_name_plural = 'HIV Status'

    def __str__(self):
        return self.name


class TBStatus(models.Model):
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
        verbose_name = 'TB Status'
        verbose_name_plural = 'TB Status'

    def __str__(self):
        return self.name


class ResultSharingChoice(models.Model):
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
        verbose_name = 'Result Sharing Choice'
        verbose_name_plural = 'Result Sharing Choices'

    def __str__(self):
        return self.name
