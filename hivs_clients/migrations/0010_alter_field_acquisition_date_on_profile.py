# Generated by Django 2.0.7 on 2018-10-05 13:27

from django.db import migrations, models
import hivs_utils.datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_clients', '0009_add_field_acuisition_date_to_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='acquisition_date',
            field=models.DateTimeField(default=hivs_utils.datetime.today, verbose_name='acquisition date'),
        ),
    ]