# Generated by Django 2.0.3 on 2018-03-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20180328_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]