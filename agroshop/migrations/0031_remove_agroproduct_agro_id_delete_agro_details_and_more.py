# Generated by Django 4.0 on 2022-01-11 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0030_remove_agro_details_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agroproduct',
            name='agro_id',
        ),
        migrations.DeleteModel(
            name='agro_details',
        ),
        migrations.DeleteModel(
            name='agroproduct',
        ),
    ]
