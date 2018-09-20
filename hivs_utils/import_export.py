from django.apps import apps
from import_export import resources


Gender = apps.get_model('hivs_utils', 'Gender')
MartialStatus = apps.get_model('hivs_utils', 'MartialStatus')
PregnancyStatus = apps.get_model('hivs_utils', 'PregnancyStatus')
AttendanceType = apps.get_model('hivs_utils', 'AttendanceType')
HIVStatus = apps.get_model('hivs_utils', 'HIVStatus')
TBStatus = apps.get_model('hivs_utils', 'TBStatus')
ResultSharingChoice = apps.get_model('hivs_utils', 'ResultSharingChoice')


class GenderResource(resources.ModelResource):

    class Meta:
        model = Gender


class MartialStatusResource(resources.ModelResource):

    class Meta:
        model = MartialStatus


class PregnancyStatusResource(resources.ModelResource):

    class Meta:
        model = PregnancyStatus


class AttendanceTypeResource(resources.ModelResource):

    class Meta:
        model = AttendanceType


class HIVStatusResource(resources.ModelResource):

    class Meta:
        model = HIVStatus


class TBStatusResource(resources.ModelResource):

    class Meta:
        model = TBStatus


class ResultSharingChoiceResource(resources.ModelResource):

    class Meta:
        model = ResultSharingChoice
