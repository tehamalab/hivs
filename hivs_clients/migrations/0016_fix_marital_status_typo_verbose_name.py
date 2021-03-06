# Generated by Django 2.1.3 on 2018-11-21 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_clients', '0015_remove_profile_geolocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='martial_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_profiles', to='hivs_utils.MartialStatus', verbose_name='marital status'),
        ),
    ]
