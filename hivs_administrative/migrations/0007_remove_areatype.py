# Generated by Django 2.0.7 on 2018-09-20 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_administrative', '0006_add area type model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='area_type',
        ),
        migrations.DeleteModel(
            name='AreaType',
        ),
        migrations.DeleteModel(
            name='AbstractAreaType',
        ),
    ]