# Generated by Django 3.0.7 on 2020-06-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_webapps_screenshot3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webapps',
            name='main_picture',
            field=models.ImageField(default='webapps/internet.png', upload_to='webapps/'),
        ),
        migrations.AlterField(
            model_name='webapps',
            name='screenshot1',
            field=models.ImageField(blank=True, default='webapps/internet.png', upload_to='webapps/'),
        ),
        migrations.AlterField(
            model_name='webapps',
            name='screenshot2',
            field=models.ImageField(blank=True, default='webapps/internet.png', upload_to='webapps/'),
        ),
        migrations.AlterField(
            model_name='webapps',
            name='screenshot3',
            field=models.ImageField(blank=True, default='webapps/internet.png', upload_to='webapps/'),
        ),
    ]
