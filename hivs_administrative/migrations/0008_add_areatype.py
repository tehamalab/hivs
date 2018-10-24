# Generated by Django 2.0.7 on 2018-09-20 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_administrative', '0007_remove_areatype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
            ],
            options={
                'verbose_name': 'Area type',
                'verbose_name_plural': 'Area types',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='area',
            name='area_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areas', to='hivs_administrative.AreaType', verbose_name='area type'),
        ),
    ]