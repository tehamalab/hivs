# Generated by Django 2.0.7 on 2018-11-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_utils', '0007_rename_model_councellingtype_to_counsellingtype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counsellingtype',
            options={'verbose_name': 'Counselling type', 'verbose_name_plural': 'Counselling types'},
        ),
    ]