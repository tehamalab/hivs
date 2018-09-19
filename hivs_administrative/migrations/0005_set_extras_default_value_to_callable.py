# Generated by Django 2.0.7 on 2018-09-19 12:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_administrative', '0004_add_field_population_source_on_area_and_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, verbose_name='Extras'),
        ),
        migrations.AlterField(
            model_name='street',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, verbose_name='extras'),
        ),
    ]