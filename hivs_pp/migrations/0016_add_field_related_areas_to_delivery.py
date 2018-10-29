# Generated by Django 2.0.7 on 2018-10-29 09:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_pp', '0015_add_field_area_to_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='related_areas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, editable=False, null=True, size=None, verbose_name='related areas'),
        ),
    ]
