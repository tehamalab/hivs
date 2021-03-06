# Generated by Django 2.0.7 on 2018-09-19 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hivs_utils', '0002_add_resultsharingchoice_model'),
        ('hivs_htc', '0011_add_field_referrer_type_to_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='test_result',
        ),
        migrations.AddField(
            model_name='register',
            name='hiv_test_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_register_results', to='hivs_utils.HIVStatus', verbose_name='HIV test result'),
        ),
        migrations.AlterField(
            model_name='register',
            name='attendance_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_registers', to='hivs_utils.AttendanceType', verbose_name='attendance type'),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_registers', to='hivs_utils.Gender', verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='register',
            name='martial_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_registers', to='hivs_utils.MartialStatus', verbose_name='martial status'),
        ),
        migrations.AlterField(
            model_name='register',
            name='pregnancy_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_registers', to='hivs_utils.PregnancyStatus', verbose_name='pregnancy status'),
        ),
        migrations.AlterField(
            model_name='register',
            name='tb_test_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_register_results', to='hivs_utils.TBStatus', verbose_name='TB test result'),
        ),
        migrations.AlterField(
            model_name='register',
            name='test_result_share',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='htc_register_results', to='hivs_utils.ResultSharingChoice', verbose_name='result sharing'),
        ),
    ]
