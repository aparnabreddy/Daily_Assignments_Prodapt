# Generated by Django 3.2.6 on 2021-08-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productname', models.CharField(max_length=25)),
                ('Productdetails', models.CharField(max_length=50)),
                ('Sellername', models.CharField(max_length=50)),
                ('Manufacturename', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('Manufacturingdate', models.CharField(max_length=25)),
                ('Expirydate', models.CharField(max_length=25)),
            ],
        ),
    ]