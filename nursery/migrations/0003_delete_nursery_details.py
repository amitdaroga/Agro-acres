# Generated by Django 4.0 on 2022-01-08 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0002_alter_nursery_details_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='nursery_details',
        ),
    ]
