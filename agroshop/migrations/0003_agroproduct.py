# Generated by Django 4.0 on 2022-01-07 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0002_rename_state_agro_details_city_agro_details_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='agroproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('pro_description', models.CharField(max_length=200)),
                ('pro_category', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('pro_quantity', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='media/agroproduct')),
                ('agro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroshop.agro_details')),
            ],
        ),
    ]
