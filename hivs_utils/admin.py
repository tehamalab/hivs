from django.contrib.postgres.fields import JSONField
from django_postgres_utils.widgets import AdminHStoreWidget


class BaseAdmin:
    formfield_overrides = {
        JSONField: {'widget': AdminHStoreWidget},
    }
