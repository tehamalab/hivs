# Generated by Django 2.0.7 on 2018-09-19 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_administrative', '0005_set_extras_default_value_to_callable'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractAreaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
            ],
            options={
                'verbose_name': 'Area type',
                'verbose_name_plural': 'Area types',
            },
        ),
        migrations.CreateModel(
            name='AreaType',
            fields=[
                ('abstractareatype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hivs_administrative.AbstractAreaType')),
            ],
            bases=('hivs_administrative.abstractareatype',),
        ),
        migrations.AddField(
            model_name='area',
            name='area_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areas', to='hivs_administrative.AreaType', verbose_name='area type'),
        ),
    ]