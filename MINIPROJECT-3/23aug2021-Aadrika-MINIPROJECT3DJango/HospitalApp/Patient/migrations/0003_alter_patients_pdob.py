# Generated by Django 3.2.6 on 2021-08-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20210820_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='pdob',
            field=models.CharField(max_length=20),
        ),
    ]
