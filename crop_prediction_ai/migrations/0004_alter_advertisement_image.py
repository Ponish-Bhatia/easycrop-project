# Generated by Django 3.2.3 on 2021-07-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop_prediction_ai', '0003_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
