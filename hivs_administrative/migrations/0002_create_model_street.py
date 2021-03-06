# Generated by Django 2.0.7 on 2018-08-02 08:53

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_administrative', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('code', models.CharField(blank=True, max_length=50, verbose_name='code')),
                ('location_description_auto', models.CharField(blank=True, help_text='can be generated automatically', max_length=255, verbose_name='location description')),
                ('population', models.PositiveIntegerField(blank=True, null=True, verbose_name='population')),
                ('population_male', models.PositiveIntegerField(blank=True, null=True, verbose_name='male population')),
                ('population_female', models.PositiveIntegerField(blank=True, null=True, verbose_name='female population')),
                ('households', models.PositiveIntegerField(blank=True, null=True, verbose_name='number of households')),
                ('population_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='population year')),
                ('geometry', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, geography=True, null=True, srid=4326, verbose_name='geometry')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='extras')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='hivs_administrative.Area', verbose_name='administrative area')),
            ],
            options={
                'verbose_name': 'Street',
                'verbose_name_plural': 'Streets',
                'abstract': False,
            },
        ),
    ]
