# Generated by Django 3.0.7 on 2020-06-07 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200607_0801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webapps',
            options={'ordering': ['-pub_date']},
        ),
    ]
