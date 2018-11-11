from django.apps import apps
from import_export import resources


Gender = apps.get_model('hivs_utils', 'Gender')
MartialStatus = apps.get_model('hivs_utils', 'MartialStatus')
EducationLevel = apps.get_model('hivs_utils', 'EducationLevel')
Occupation = apps.get_model('hivs_utils', 'Occupation')
PregnancyStatus = apps.get_model('hivs_utils', 'PregnancyStatus')
AttendanceType = apps.get_model('hivs_utils', 'AttendanceType')
CounsellingType = apps.get_model('hivs_utils', 'CounsellingType')
HIVStatus = apps.get_model('hivs_utils', 'HIVStatus')
TBStatus = apps.get_model('hivs_utils', 'TBStatus')
ResultSharingChoice = apps.get_model('hivs_utils', 'ResultSharingChoice')
Topic = apps.get_model('hivs_utils', 'Topic')


class GenderResource(resources.ModelResource):

    class Meta:
        model = Gender


class MartialStatusResource(resources.ModelResource):

    class Meta:
        model = MartialStatus


class EducationLevelResource(resources.ModelResource):

    class Meta:
        model = EducationLevel


class OccupationResource(resources.ModelResource):

    class Meta:
        model = Occupation


class PregnancyStatusResource(resources.ModelResource):

    class Meta:
        model = PregnancyStatus


class AttendanceTypeResource(resources.ModelResource):

    class Meta:
        model = AttendanceType


class CounsellingTypeResource(resources.ModelResource):

    class Meta:
        model = CounsellingType


class HIVStatusResource(resources.ModelResource):

    class Meta:
        model = HIVStatus


class TBStatusResource(resources.ModelResource):

    class Meta:
        model = TBStatus


class ResultSharingChoiceResource(resources.ModelResource):

    class Meta:
        model = ResultSharingChoice


class TopicResource(resources.ModelResource):

    class Meta:
        model = Topic
