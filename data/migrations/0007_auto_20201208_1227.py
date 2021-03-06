# Generated by Django 3.1.3 on 2020-12-08 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20201208_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='date',
        ),
        migrations.RemoveField(
            model_name='items',
            name='issue_quantity',
        ),
        migrations.RemoveField(
            model_name='items',
            name='price',
        ),
        migrations.RemoveField(
            model_name='items',
            name='recieve_quantity',
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_quantity', models.IntegerField(null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('recieve_quantity', models.IntegerField(default='0', null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demands', to='data.items')),
            ],
        ),
    ]
