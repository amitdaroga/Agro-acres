# Generated by Django 4.0 on 2022-01-13 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_customer_details'),
        ('agroshop', '0034_initial'),
        ('farmer', '0012_addtocart_f'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addtocart_f',
            new_name='faraddtocart',
        ),
    ]
