# Generated by Django 4.0.4 on 2022-05-18 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme_review_book',
            options={'ordering': ['title_theme_review'], 'verbose_name': 'Тема обзора на книг', 'verbose_name_plural': 'Тема обзора на книг'},
        ),
    ]