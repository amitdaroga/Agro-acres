# Generated by Django 4.0 on 2022-01-18 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0038_product_remove_agroproduct_agro_id'),
        ('farmer', '0013_rename_addtocart_f_faraddtocart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faraddtocart',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroshop.product'),
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
