# Generated by Django 3.1.3 on 2020-12-08 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20201207_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='yearly_demand',
            new_name='average_daily_demand',
        ),
        migrations.RemoveField(
            model_name='items',
            name='no_of_workingdays',
        ),
    ]
