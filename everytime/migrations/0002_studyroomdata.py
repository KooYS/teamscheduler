# Generated by Django 2.0.4 on 2018-05-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everytime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyRoomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=5)),
                ('offTime', models.IntegerField(null=True)),
            ],
        ),
    ]
