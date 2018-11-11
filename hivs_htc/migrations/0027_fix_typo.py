# Generated by Django 2.0.7 on 2018-11-11 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_htc', '0026_rename_counselling_type_to_counselling_type_on_register'),
        ('hivs_utils', '0007_rename_model_councellingtype_to_counsellingtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='counselling_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_registers', to='hivs_utils.CounsellingType', verbose_name='counselling type'),
        ),
    ]
