# Generated by Django 2.0.7 on 2018-10-25 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_htc', '0014_alter_verbose_name_issuer_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referral_center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_referrals', to='hivs_htc.ReferralCenter', verbose_name='referred to'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='referrer_center',
            field=models.ForeignKey(blank=True, help_text='center that issues the referral', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_referrers', to='hivs_htc.ReferralCenter', verbose_name='referred from'),
        ),
    ]