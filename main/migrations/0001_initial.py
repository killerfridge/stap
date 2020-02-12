# Generated by Django 3.0.3 on 2020-02-12 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='STP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.STP')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.DecimalField(decimal_places=2, max_digits=20)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Site')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Year')),
            ],
        ),
        migrations.CreateModel(
            name='Beds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general', models.IntegerField()),
                ('critical', models.IntegerField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Site')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Year')),
            ],
        ),
    ]