# Generated by Django 3.0.7 on 2020-06-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
