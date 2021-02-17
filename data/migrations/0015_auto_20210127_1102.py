# Generated by Django 3.1.3 on 2021-01-27 05:32

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20201209_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='carrying_cost',
            field=models.PositiveIntegerField(default='15', help_text='Enter as percentage of unit cost', validators=[data.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='items',
            name='lead_time',
            field=models.PositiveIntegerField(blank=True, default='5', null=True, validators=[data.models.validate_zero]),
        ),
        migrations.AlterField(
            model_name='items',
            name='service_level',
            field=models.PositiveIntegerField(blank=True, default='95', null=True, validators=[data.models.validate_even]),
        ),
    ]
