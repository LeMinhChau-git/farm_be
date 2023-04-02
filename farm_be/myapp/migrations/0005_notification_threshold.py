# Generated by Django 3.1 on 2023-03-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_device_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('content', models.TextField()),
                ('state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Threshold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]