# Generated by Django 3.1.3 on 2020-11-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20201120_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='carrying_cost',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='ordering_cost',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='present_inventory',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='demand',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='demand',
            name='total',
            field=models.PositiveIntegerField(null=True),
        ),
    ]