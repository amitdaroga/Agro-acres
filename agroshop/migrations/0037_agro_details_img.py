# Generated by Django 4.0 on 2022-01-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0036_remove_agro_details_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='agro_details',
            name='img',
            field=models.FileField(default='media/profile/default.png', upload_to='media/profile'),
        ),
    ]
