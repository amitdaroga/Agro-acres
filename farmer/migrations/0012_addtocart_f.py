# Generated by Django 4.0 on 2022-01-13 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_customer_details'),
        ('agroshop', '0034_initial'),
        ('farmer', '0011_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addtocart_f',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroshop.agroproduct')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.user')),
            ],
        ),
    ]
