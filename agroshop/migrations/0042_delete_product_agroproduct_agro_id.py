# Generated by Django 4.0 on 2022-01-18 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0016_alter_faraddtocart_p_id'),
        ('agroshop', '0041_agroproduct_remove_product_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product',
        ),
        migrations.AddField(
            model_name='agroproduct',
            name='agro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroshop.agro_details'),
        ),
    ]
