from django.apps import apps
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django_postgres_utils.widgets import AdminHStoreWidget
from import_export.admin import ImportExportModelAdmin
from .import_export import (
    GenderResource,
    MaritalStatusResource,
    EducationLevelResource,
    OccupationResource,
    PregnancyStatusResource,
    AttendanceTypeResource,
    CounsellingTypeResource,
    HIVStatusResource,
    TBStatusResource,
    ResultSharingChoiceResource,
    TopicResource
)


Gender = apps.get_model('hivs_utils', 'Gender')
MaritalStatus = apps.get_model('hivs_utils', 'MaritalStatus')
EducationLevel = apps.get_model('hivs_utils', 'EducationLevel')
Occupation = apps.get_model('hivs_utils', 'Occupation')
PregnancyStatus = apps.get_model('hivs_utils', 'PregnancyStatus')
AttendanceType = apps.get_model('hivs_utils', 'AttendanceType')
CounsellingType = apps.get_model('hivs_utils', 'CounsellingType')
HIVStatus = apps.get_model('hivs_utils', 'HIVStatus')
TBStatus = apps.get_model('hivs_utils', 'TBStatus')
ResultSharingChoice = apps.get_model('hivs_utils', 'ResultSharingChoice')
Topic = apps.get_model('hivs_utils', 'Topic')


class BaseAdmin:
    formfield_overrides = {
        JSONField: {'widget': AdminHStoreWidget},
    }


class ChoiceAdmin(BaseAdmin, ImportExportModelAdmin):
    list_display = ['id', 'name', 'code']
    list_display_links = ['id', 'name']
    ordering = ['id']


@admin.register(Gender)
class GenderAdmin(ChoiceAdmin):
    resource_class = GenderResource


@admin.register(MaritalStatus)
class MaritalStatusAdmin(ChoiceAdmin):
    resource_class = MaritalStatusResource


@admin.register(EducationLevel)
class EducationLevelAdmin(ChoiceAdmin):
    resource_class = EducationLevelResource


@admin.register(Occupation)
class OccupationAdmin(ChoiceAdmin):
    resource_class = OccupationResource


@admin.register(PregnancyStatus)
class PregnancyStatusAdmin(ChoiceAdmin):
    resource_class = PregnancyStatusResource


@admin.register(AttendanceType)
class AttendanceTypeAdmin(ChoiceAdmin):
    resource_class = AttendanceTypeResource


@admin.register(CounsellingType)
class CounsellingTypeAdmin(ChoiceAdmin):
    resource_class = CounsellingTypeResource


@admin.register(HIVStatus)
class HIVStatusAdmin(ChoiceAdmin):
    resource_class = HIVStatusResource


@admin.register(TBStatus)
class TBStatusAdmin(ChoiceAdmin):
    resource_class = TBStatusResource


@admin.register(ResultSharingChoice)
class ResultSharingChoiceAdmin(ChoiceAdmin):
    resource_class = ResultSharingChoiceResource


@admin.register(Topic)
class TopicAdmin(ChoiceAdmin):
    resource_class = TopicResource
