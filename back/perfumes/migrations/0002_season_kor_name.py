# Generated by Django 3.0.4 on 2020-04-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='kor_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]