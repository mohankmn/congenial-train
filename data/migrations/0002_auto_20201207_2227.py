# Generated by Django 3.1.3 on 2020-12-07 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='service_levl',
            new_name='service_level',
        ),
    ]
