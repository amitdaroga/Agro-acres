# Generated by Django 4.0 on 2022-01-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0048_order_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_a',
            name='orderdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
