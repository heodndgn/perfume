# Generated by Django 3.0.4 on 2020-04-25 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0018_auto_20200425_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='category',
        ),
    ]
