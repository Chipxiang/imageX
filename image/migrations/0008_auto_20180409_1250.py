# Generated by Django 2.0.3 on 2018-04-09 04:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import image.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0007_image_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=image.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='image',
            name='tag',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
