# Generated by Django 4.0 on 2022-01-17 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0035_alter_agro_details_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agro_details',
            name='img',
        ),
    ]