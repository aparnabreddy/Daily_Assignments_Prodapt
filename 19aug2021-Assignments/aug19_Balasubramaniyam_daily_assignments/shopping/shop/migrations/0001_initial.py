# Generated by Django 3.2.6 on 2021-08-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]
