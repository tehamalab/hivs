# Generated by Django 2.0.7 on 2018-11-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_htc', '0028_fix_typo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='counselled_after_test',
            field=models.BooleanField(default=False, verbose_name='counselled after test'),
        ),
    ]