# Generated by Django 3.2.6 on 2021-08-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pdetails', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
