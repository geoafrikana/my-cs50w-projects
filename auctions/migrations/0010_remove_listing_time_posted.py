# Generated by Django 3.1.3 on 2020-12-18 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201218_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='time_posted',
        ),
    ]
