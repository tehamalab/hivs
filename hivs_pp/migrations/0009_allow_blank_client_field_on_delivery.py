# Generated by Django 2.0.7 on 2018-10-25 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_pp', '0008_add_service_confidential_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pp_deliveries', to='hivs_clients.Profile', verbose_name='client profile'),
        ),
    ]
