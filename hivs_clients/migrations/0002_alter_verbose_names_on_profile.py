# Generated by Django 2.0.7 on 2018-08-01 20:01

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='birthdate'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='geolocation',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326, verbose_name='geolocation'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='middle name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_phones',
            field=django.contrib.postgres.fields.ArrayField(base_field=phonenumber_field.modelfields.PhoneNumberField(max_length=128), blank=True, default=[], size=None, verbose_name='other phones'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='phone number'),
        ),
    ]
