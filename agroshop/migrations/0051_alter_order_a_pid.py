# Generated by Django 4.0 on 2022-01-31 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0050_remove_order_a_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_a',
            name='pid',
            field=models.CharField(max_length=100),
        ),
    ]
