# Generated by Django 3.2.6 on 2021-08-26 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_no', models.CharField(max_length=10)),
                ('owner_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('aadhar_no', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]