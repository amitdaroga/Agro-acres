# Generated by Django 4.0 on 2022-01-31 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0051_alter_order_a_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_a',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroshop.agroproduct'),
        ),
    ]
