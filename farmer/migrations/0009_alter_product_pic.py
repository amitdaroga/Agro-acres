# Generated by Django 4.0 on 2022-01-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0008_rename_agro_id_product_far_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.FileField(upload_to='media/farproduct'),
        ),
    ]
