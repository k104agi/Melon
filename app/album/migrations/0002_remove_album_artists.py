# Generated by Django 2.0.2 on 2018-02-22 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artists',
        ),
    ]
