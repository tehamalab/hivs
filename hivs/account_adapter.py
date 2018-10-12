from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse

        (Comment reproduced from the overridden method.)
        """
        return getattr(settings, 'ACCOUNT_OPEN_FOR_SIGNUP', False)
