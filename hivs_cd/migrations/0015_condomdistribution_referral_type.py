# Generated by Django 2.0.7 on 2018-11-08 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_htc', '0017_add_register_occupation'),
        ('hivs_cd', '0014_remove_condomdistribution_referral_given_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='condomdistribution',
            name='referral_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='condom_distriputions', to='hivs_htc.ReferralCenterType', verbose_name='type of referral given'),
        ),
    ]
