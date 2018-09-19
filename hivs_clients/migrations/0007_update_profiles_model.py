# Generated by Django 2.0.7 on 2018-09-19 20:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_clients', '0006_set_extras_default_value_to_callable'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last modified'),
        ),
        migrations.AddField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_profiles', to='hivs_utils.Gender', verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='martial_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_profiles', to='hivs_utils.MartialStatus', verbose_name='martial status'),
        ),
    ]
