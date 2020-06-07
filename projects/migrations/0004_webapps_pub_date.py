# Generated by Django 3.0.7 on 2020-06-06 20:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_webapps'),
    ]

    operations = [
        migrations.AddField(
            model_name='webapps',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 6, 6, 20, 28, 45, 472100, tzinfo=utc)),
            preserve_default=False,
        ),
    ]