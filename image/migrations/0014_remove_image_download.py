# Generated by Django 2.0.3 on 2018-04-26 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0013_image_download'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='download',
        ),
    ]