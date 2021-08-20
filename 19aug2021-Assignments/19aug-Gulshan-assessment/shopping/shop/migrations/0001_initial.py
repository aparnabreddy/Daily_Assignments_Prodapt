# Generated by Django 3.2.6 on 2021-08-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shopname', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
            ],
        ),
    ]
