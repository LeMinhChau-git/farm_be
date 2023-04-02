# Generated by Django 3.1 on 2023-03-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_airhumidity_lightintensitive_soilmoisure_temprature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=30)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
