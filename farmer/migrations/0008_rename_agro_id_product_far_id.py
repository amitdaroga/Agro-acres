# Generated by Django 4.0 on 2022-01-10 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0007_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='agro_id',
            new_name='far_id',
        ),
    ]
