# Generated by Django 2.0.7 on 2018-08-02 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_administrative', '0002_create_model_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='streets', to='hivs_administrative.Area', verbose_name='administrative area'),
        ),
    ]
