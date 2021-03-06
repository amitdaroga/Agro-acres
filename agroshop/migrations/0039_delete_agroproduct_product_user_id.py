# Generated by Django 4.0 on 2022-01-18 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0038_product_remove_agroproduct_agro_id'),
        ('customer', '0012_customer_details'),
        ('farmer', '0014_alter_faraddtocart_p_id_delete_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='agroproduct',
        ),
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.user'),
        ),
    ]
