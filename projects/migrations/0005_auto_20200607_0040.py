# Generated by Django 3.0.7 on 2020-06-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_webapps_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webapps',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='webapps',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='webapps',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]