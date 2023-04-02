# Generated by Django 3.1 on 2023-03-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LightIntensitive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SoilMoisure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temprature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
    ]
