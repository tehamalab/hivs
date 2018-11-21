from django.apps import apps
from rest_framework import serializers


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


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'


class MaritalStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaritalStatus
        fields = '__all__'


class EducationLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationLevel
        fields = '__all__'


class OccupationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occupation
        fields = '__all__'


class PregnancyStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = PregnancyStatus
        fields = '__all__'


class AttendanceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceType
        fields = '__all__'


class CounsellingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CounsellingType
        fields = '__all__'


class HIVStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = HIVStatus
        fields = '__all__'


class TBStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = TBStatus
        fields = '__all__'


class ResultSharingChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultSharingChoice
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
