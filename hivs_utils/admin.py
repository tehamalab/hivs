from django.apps import apps
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django_postgres_utils.widgets import AdminHStoreWidget
from import_export.admin import ImportExportModelAdmin
from .import_export import (GenderResource, MartialStatusResource, EducationLevelResource,
                            PregnancyStatusResource, AttendanceTypeResource,
                            HIVStatusResource, TBStatusResource,
                            ResultSharingChoiceResource)


Gender = apps.get_model('hivs_utils', 'Gender')
MartialStatus = apps.get_model('hivs_utils', 'MartialStatus')
EducationLevel = apps.get_model('hivs_utils', 'EducationLevel')
PregnancyStatus = apps.get_model('hivs_utils', 'PregnancyStatus')
AttendanceType = apps.get_model('hivs_utils', 'AttendanceType')
HIVStatus = apps.get_model('hivs_utils', 'HIVStatus')
TBStatus = apps.get_model('hivs_utils', 'TBStatus')
ResultSharingChoice = apps.get_model('hivs_utils', 'ResultSharingChoice')


class BaseAdmin:
    formfield_overrides = {
        JSONField: {'widget': AdminHStoreWidget},
    }


@admin.register(Gender)
class GenderAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = GenderResource


@admin.register(MartialStatus)
class MartialStatusAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = MartialStatusResource


@admin.register(EducationLevel)
class EducationLevelAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = EducationLevelResource


@admin.register(PregnancyStatus)
class PregnancyStatusAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = PregnancyStatusResource


@admin.register(AttendanceType)
class AttendanceTypeAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = AttendanceTypeResource


@admin.register(HIVStatus)
class HIVStatusAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = HIVStatusResource


@admin.register(TBStatus)
class TBStatusAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = TBStatusResource


@admin.register(ResultSharingChoice)
class ResultSharingChoiceAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = ResultSharingChoiceResource
