from django.apps import apps
from django.contrib.gis import admin


Profile = apps.get_model('hivs_clients', 'Profile')


class ProfileAdmin(admin.OSMGeoAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
