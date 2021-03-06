# Generated by Django 2.0.7 on 2018-10-25 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_cd', '0005_add_field_attendance_type_from_condom_distribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condomdistribution',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='client age'),
        ),
        migrations.AlterField(
            model_name='condomdistribution',
            name='condoms_female_count',
            field=models.IntegerField(default=0, help_text='No. of male condoms delivered', validators=[django.core.validators.MinValueValidator(0)], verbose_name='No. of female condoms provided'),
        ),
        migrations.AlterField(
            model_name='condomdistribution',
            name='condoms_male_count',
            field=models.IntegerField(default=0, help_text='No. of male condoms delivered', validators=[django.core.validators.MinValueValidator(0)], verbose_name='No. of male condoms provided'),
        ),
        migrations.AlterField(
            model_name='condomdistribution',
            name='gender',
            field=models.CharField(max_length=25, verbose_name='client gender'),
        ),
    ]
