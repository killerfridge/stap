# Generated by Django 3.0.3 on 2020-02-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='nhs_code',
            field=models.CharField(default='RQM', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stp',
            name='code',
            field=models.CharField(default='E54000027', max_length=10),
            preserve_default=False,
        ),
    ]