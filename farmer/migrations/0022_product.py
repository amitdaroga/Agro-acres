# Generated by Django 4.0 on 2022-01-22 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_customer_details_img'),
        ('farmer', '0021_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('pro_description', models.CharField(max_length=200)),
                ('pro_category', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('pro_quantity', models.CharField(max_length=100)),
                ('pic', models.FileField(upload_to='media/farproduct')),
                ('enable', models.CharField(default='Enable', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.user')),
            ],
        ),
    ]
