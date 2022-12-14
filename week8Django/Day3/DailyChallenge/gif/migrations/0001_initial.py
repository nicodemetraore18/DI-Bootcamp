# Generated by Django 4.1.2 on 2022-12-11 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('URL', models.URLField()),
                ('uploader_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 11, 17, 44, 37, 890824))),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(blank=True, related_name='categories', to='gif.category')),
            ],
        ),
    ]
