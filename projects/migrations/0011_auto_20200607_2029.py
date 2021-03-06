# Generated by Django 3.0.7 on 2020-06-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rate_by_content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rate_by_creativity',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rate_by_design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rate_by_usability',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
    ]
