from django.urls import path, include
from rest_framework import routers
from hivs_administrative.api.views import AreaTypeViewSet, AreaViewSet, StreetViewSet
from hivs_clients.api.views import ProfileViewSet
from hivs_pp.api.views import CategoryViewSet, ServiceViewSet, DeliveryViewSet, DeliveryPivotViewSet
from hivs_cd.api.views import (
    CenterViewSet,
    PurposeViewSet,
    CondomDistributionViewSet,
    CondomDistributionPivotViewSet
)
from hivs_utils.api.views import (
    GenderViewSet,
    MartialStatusViewSet,
    EducationLevelViewSet,
    OccupationViewSet,
    PregnancyStatusViewSet,
    AttendanceTypeViewSet,
    CounsellingTypeViewSet,
    HIVStatusViewSet,
    TBStatusViewSet,
    ResultSharingChoiceViewSet,
    TopicViewSet
)


router = routers.DefaultRouter()
router.register(r'common/gender', GenderViewSet)
router.register(r'common/martial-status', MartialStatusViewSet)
router.register(r'common/education-levels', EducationLevelViewSet)
router.register(r'common/occupations', OccupationViewSet)
router.register(r'common/pregnancy-status', PregnancyStatusViewSet)
router.register(r'common/attenndance-types', AttendanceTypeViewSet)
router.register(r'common/counselling-types', CounsellingTypeViewSet)
router.register(r'common/hiv-status', HIVStatusViewSet)
router.register(r'common/tb-status', TBStatusViewSet)
router.register(r'common/results-sharing-choices', ResultSharingChoiceViewSet)
router.register(r'common/topics', TopicViewSet)
router.register(r'administrative/area-types', AreaTypeViewSet)
router.register(r'administrative/areas', AreaViewSet)
router.register(r'administrative/streets', StreetViewSet)
router.register(r'clients/profiles', ProfileViewSet)
router.register(r'prevention/categories', CategoryViewSet)
router.register(r'prevention/services', ServiceViewSet)
router.register(r'prevention/deliveries', DeliveryViewSet)
router.register(r'prevention/pivot', DeliveryPivotViewSet, 'delivery-pivot')
router.register(r'condom/centers', CenterViewSet)
router.register(r'condom/purposes', PurposeViewSet)
router.register(r'condom/distributions', CondomDistributionViewSet)
router.register(r'condom/pivot', CondomDistributionPivotViewSet, 'condom-pivot')


urlpatterns = [
    path('', include(router.urls)),
    path('_auth/', include('rest_framework.urls'))
]
