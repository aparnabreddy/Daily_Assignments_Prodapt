# Generated by Django 3.2.6 on 2021-08-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passengers', '0002_alter_passenger_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('from_station', models.CharField(max_length=40)),
                ('to_station', models.CharField(max_length=40)),
                ('DOJ', models.DateField()),
            ],
        ),
    ]
