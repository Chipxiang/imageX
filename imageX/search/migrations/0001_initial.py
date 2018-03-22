# Generated by Django 2.0.3 on 2018-03-22 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_tag', models.CharField(max_length=200)),
                ('image_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Member'),
        ),
    ]
