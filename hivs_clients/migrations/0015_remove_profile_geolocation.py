# Generated by Django 2.0.7 on 2018-11-18 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_clients', '0014_allow_blank_occupation_and_education_on_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='geolocation',
        ),
    ]
