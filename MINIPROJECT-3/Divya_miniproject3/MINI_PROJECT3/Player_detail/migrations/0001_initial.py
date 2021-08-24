# Generated by Django 3.2.6 on 2021-08-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Game', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Place', models.IntegerField()),
                ('Medal', models.CharField(max_length=50)),
            ],
        ),
    ]