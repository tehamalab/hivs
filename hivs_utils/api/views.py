from django.apps import apps
from rest_framework import viewsets
from .serializers import (
    GenderSerializer,
    MartialStatusSerializer,
    EducationLevelSerializer,
    OccupationSerializer,
    PregnancyStatusSerializer,
    AttendanceTypeSerializer,
    CounsellingTypeSerializer,
    HIVStatusSerializer,
    TBStatusSerializer,
    ResultSharingChoiceSerializer,
    TopicSerializer
)


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


class BaseViewSet(viewsets.ModelViewSet):
    filterset_fields = {
        'name': ['exact', 'iexact', 'icontains'],
        'code': ['exact'],
    }
    ordering = ['name']


class GenderViewSet(BaseViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class MartialStatusViewSet(BaseViewSet):
    queryset = MartialStatus.objects.all()
    serializer_class = MartialStatusSerializer


class EducationLevelViewSet(BaseViewSet):
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer


class OccupationViewSet(BaseViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer


class PregnancyStatusViewSet(BaseViewSet):
    queryset = PregnancyStatus.objects.all()
    serializer_class = PregnancyStatusSerializer


class AttendanceTypeViewSet(BaseViewSet):
    queryset = AttendanceType.objects.all()
    serializer_class = AttendanceTypeSerializer


class CounsellingTypeViewSet(BaseViewSet):
    queryset = CounsellingType.objects.all()
    serializer_class = CounsellingTypeSerializer


class HIVStatusViewSet(BaseViewSet):
    queryset = HIVStatus.objects.all()
    serializer_class = HIVStatusSerializer


class TBStatusViewSet(BaseViewSet):
    queryset = TBStatus.objects.all()
    serializer_class = TBStatusSerializer


class ResultSharingChoiceViewSet(BaseViewSet):
    queryset = ResultSharingChoice.objects.all()
    serializer_class = ResultSharingChoiceSerializer


class TopicViewSet(BaseViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
