# Generated by Django 3.2.6 on 2021-08-19 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='email',
        ),
    ]
