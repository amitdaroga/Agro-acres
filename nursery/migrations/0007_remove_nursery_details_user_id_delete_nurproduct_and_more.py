# Generated by Django 4.0 on 2022-01-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0006_rename_far_id_nurproduct_nur_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery_details',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='nurproduct',
        ),
        migrations.DeleteModel(
            name='nursery_details',
        ),
    ]