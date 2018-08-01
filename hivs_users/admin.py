from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CoreUserAdmin
from .models import User


class UserAdmin(CoreUserAdmin):
    pass


admin.site.register(User, UserAdmin)
