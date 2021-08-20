# Generated by Django 3.2.6 on 2021-08-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellername', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phoneno', models.BigIntegerField()),
                ('dob', models.CharField(max_length=25)),
                ('district', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('adhaarno', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]