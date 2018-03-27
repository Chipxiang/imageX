# Generated by Django 2.0.3 on 2018-03-27 14:22

import django.core.validators
from django.db import migrations, models
import image.models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=image.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg'])]),
        ),
    ]
