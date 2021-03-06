# Generated by Django 2.0.7 on 2018-09-20 08:21

import django.contrib.postgres.fields
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_clients', '0007_update_profiles_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='other_phones',
            field=django.contrib.postgres.fields.ArrayField(base_field=phonenumber_field.modelfields.PhoneNumberField(max_length=128), blank=True, default=list, size=None, verbose_name='other phones'),
        ),
    ]
