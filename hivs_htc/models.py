from .abstract_models import (AbstractRegister, AbstractReferralCenterType,
                              AbstractReferralCenter, AbstractReferral)


class Register(AbstractRegister):
    pass


class ReferralCenterType(AbstractReferralCenterType):
    pass


class ReferralCenter(AbstractReferralCenter):
    pass


class Referral(AbstractReferral):
    pass
