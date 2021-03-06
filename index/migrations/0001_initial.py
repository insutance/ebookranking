# Generated by Django 3.1 on 2020-09-17 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookstore', models.CharField(max_length=20)),
                ('rank', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('link', models.URLField()),
                ('author', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TotalBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('author', models.CharField(default='', max_length=100)),
                ('image', models.URLField(default='')),
                ('kyoboPrice', models.IntegerField(default=0)),
                ('yes24Price', models.IntegerField(default=0)),
                ('aladinPrice', models.IntegerField(default=0)),
                ('naverPrice', models.IntegerField(default=0)),
                ('ridibooksPrice', models.IntegerField(default=0)),
                ('kyoboLink', models.URLField(default='')),
                ('yes24Link', models.URLField(default='')),
                ('aladinLink', models.URLField(default='')),
                ('naverLink', models.URLField(default='')),
                ('ridibooksLink', models.URLField(default='')),
                ('rank', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
