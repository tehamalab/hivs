# Generated by Django 2.0.7 on 2018-09-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_htc', '0005_add_register_fk_to_referral_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='unique_info',
            field=models.TextField(blank=True, help_text='Example; allergy', verbose_name='unique information'),
        ),
    ]
