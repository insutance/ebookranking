# Generated by Django 3.1 on 2020-09-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='totalbooks',
            name='aladinPrice',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='totalbooks',
            name='kyoboPrice',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='totalbooks',
            name='naverPrice',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='totalbooks',
            name='ridibooksPrice',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='totalbooks',
            name='yes24Price',
            field=models.CharField(max_length=20),
        ),
    ]