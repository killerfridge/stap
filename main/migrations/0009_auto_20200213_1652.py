# Generated by Django 3.0.3 on 2020-02-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_subsite_main_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subsite',
            options={'ordering': ['-main_location', 'name']},
        ),
        migrations.AddField(
            model_name='income',
            name='forecast_surplus',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='nhs_code',
            field=models.CharField(max_length=6, unique=True, verbose_name='NHS Code'),
        ),
        migrations.AlterField(
            model_name='subsite',
            name='nhs_code',
            field=models.CharField(max_length=6, unique=True, verbose_name='NHS Code'),
        ),
    ]
