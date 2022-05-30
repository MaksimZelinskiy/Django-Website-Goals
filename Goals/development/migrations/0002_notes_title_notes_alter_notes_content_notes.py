# Generated by Django 4.0.4 on 2022-05-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='title_notes',
            field=models.CharField(blank=True, max_length=100, verbose_name='Нахвание заметки'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='content_notes',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Текст заметки'),
        ),
    ]
