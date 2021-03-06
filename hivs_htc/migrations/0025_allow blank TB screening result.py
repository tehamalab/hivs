# Generated by Django 2.0.7 on 2018-11-11 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_htc', '0024_change_verbose_name_of_register_on_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='tb_screening_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_register_screening', to='hivs_utils.TBStatus', verbose_name='TB screening result'),
        ),
    ]
