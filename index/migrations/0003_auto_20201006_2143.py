# Generated by Django 3.1 on 2020-10-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20201006_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
