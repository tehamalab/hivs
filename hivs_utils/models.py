from django.utils.translation import ugettext_lazy as _
from .abstract_models import AbstractChoice


class Gender(AbstractChoice):

    class Meta:
        verbose_name = _('Gender')
        verbose_name_plural = _('Gender')


class MartialStatus(AbstractChoice):

    class Meta:
        verbose_name = _('Martial status')
        verbose_name_plural = _('Martial status')


class EducationLevel(AbstractChoice):

    class Meta:
        verbose_name = _('Education level')
        verbose_name_plural = _('Education levels')


class Occupation(AbstractChoice):

    class Meta:
        verbose_name = _('Occupation')
        verbose_name_plural = _('Occupations')


class PregnancyStatus(AbstractChoice):

    class Meta:
        verbose_name = _('Pregnancy status')
        verbose_name_plural = _('Pregnancy status')


class AttendanceType(AbstractChoice):

    class Meta:
        verbose_name = _('Attendance type')
        verbose_name_plural = _('Attendance types')


class CounsellingType(AbstractChoice):

    class Meta:
        verbose_name = _('Counselling type')
        verbose_name_plural = _('Counselling types')


class HIVStatus(AbstractChoice):

    class Meta:
        verbose_name = _('HIV Status')
        verbose_name_plural = _('HIV Status')


class TBStatus(AbstractChoice):

    class Meta:
        verbose_name = _('TB Status')
        verbose_name_plural = _('TB Status')


class ResultSharingChoice(AbstractChoice):

    class Meta:
        verbose_name = _('Result Sharing Choice')
        verbose_name_plural = _('Result Sharing Choices')


class Topic(AbstractChoice):

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')
