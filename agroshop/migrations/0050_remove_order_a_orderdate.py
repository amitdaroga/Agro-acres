# Generated by Django 4.0 on 2022-01-31 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0049_alter_order_a_orderdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_a',
            name='orderdate',
        ),
    ]
