# Generated by Django 4.0 on 2022-01-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0008_agroproduct_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agroproduct',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
