# Generated by Django 4.0 on 2022-01-22 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0023_remove_farmer_details_user_id_and_more'),
        ('agroshop', '0043_alter_agroproduct_pic'),
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