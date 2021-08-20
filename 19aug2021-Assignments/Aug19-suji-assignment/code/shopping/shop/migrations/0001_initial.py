# Generated by Django 3.2.6 on 2021-08-19 13:01

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
                ('shopname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('phoneno', models.BigIntegerField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
