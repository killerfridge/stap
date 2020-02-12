# Generated by Django 3.0.3 on 2020-02-12 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200212_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beds',
            options={'ordering': ['-year'], 'verbose_name_plural': 'Beds'},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['-year'], 'verbose_name_plural': 'Income Statements'},
        ),
        migrations.AlterModelOptions(
            name='stp',
            options={'ordering': ['name'], 'verbose_name': 'STP/Health Board', 'verbose_name_plural': 'STPs/Health Boards'},
        ),
    ]
