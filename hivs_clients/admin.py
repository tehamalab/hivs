from django.apps import apps
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from hivs_utils.admin import BaseAdmin
from .import_export import ProfileResource


Profile = apps.get_model('hivs_clients', 'Profile')

try:
    Delivery = apps.get_registered_model('hivs_pp', 'Delivery')
except LookupError:
    Delivery = None


class DeliveryInline(admin.StackedInline):
    model = Delivery
    exclude = ['time', 'gender', 'age', 'extras']
    filter_horizontal = ['services']


if Delivery is not None:
    profile_inlines = [DeliveryInline]
else:
    profile_inlines = None


@admin.register(Profile)
class ProfileAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = ProfileResource
    readonly_fields = ['id', 'timestamp', 'last_modified']
    list_display = ['id', 'first_name', 'last_name', 'registration_id']
    list_display_links = ['id', 'first_name', 'last_name']
    list_filter = ['gender', 'martial_status', 'timestamp']
    search_fields = ['id', 'first_name', 'last_name', 'registration_id',
                     'area__name', 'street__name']
    inlines = profile_inlines
