# Generated by Django 2.0.7 on 2018-08-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_pp', '0002_change_verbose_name_on_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='review_date',
            field=models.DateField(blank=True, null=True, verbose_name='review date'),
        ),
    ]
