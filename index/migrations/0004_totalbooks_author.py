# Generated by Django 3.1 on 2020-08-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200819_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalbooks',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
    ]
