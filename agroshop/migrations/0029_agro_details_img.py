# Generated by Django 4.0 on 2022-01-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroshop', '0028_remove_agro_details_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='agro_details',
            name='img',
            field=models.FileField(default=1, upload_to='media/profile'),
            preserve_default=False,
        ),
    ]