# Generated by Django 3.0.3 on 2020-02-12 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_subsite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsite',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Site', verbose_name='Trust'),
        ),
    ]
