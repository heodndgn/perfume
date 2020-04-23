# Generated by Django 3.0.5 on 2020-04-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0002_auto_20200409_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfume',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='perfume',
            name='notes',
        ),
        migrations.AddField(
            model_name='perfume',
            name='base_notes',
            field=models.ManyToManyField(related_name='perfumes_base', to='perfumes.Note'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='heart_notes',
            field=models.ManyToManyField(related_name='perfumes_heart', to='perfumes.Note'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='top_notes',
            field=models.ManyToManyField(related_name='perfumes_top', to='perfumes.Note'),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='thumbnail',
            field=models.CharField(max_length=200),
        ),
    ]