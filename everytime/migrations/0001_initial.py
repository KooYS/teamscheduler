# Generated by Django 2.0.4 on 2018-05-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exist_class', models.CharField(default=None, max_length=300)),
                ('building_name', models.CharField(default=None, max_length=20)),
                ('floor', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ClassPerDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_name', models.CharField(max_length=10)),
                ('class_data', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EveryTimeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawling_data', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParsedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_parsing', models.CharField(max_length=100)),
            ],
        ),
    ]
