# Generated by Django 2.0.7 on 2018-10-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_utils', '0002_add_resultsharingchoice_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=25, verbose_name='code')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
            ],
            options={
                'verbose_name': 'Education level',
                'verbose_name_plural': 'Education levels',
            },
        ),
    ]
