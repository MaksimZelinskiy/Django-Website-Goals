# Generated by Django 4.0.4 on 2022-05-16 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category_notes', models.CharField(db_index=True, max_length=30, verbose_name='Наименование категории заметки')),
            ],
            options={
                'verbose_name': 'Категория заметки',
                'verbose_name_plural': 'Категории заметок',
                'ordering': ['title_category_notes'],
            },
        ),
        migrations.CreateModel(
            name='Category_routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category_routine', models.CharField(db_index=True, max_length=30, verbose_name='Наименование категории распорядка')),
            ],
            options={
                'verbose_name': 'Категория распорядка',
                'verbose_name_plural': 'Категории распорядка',
                'ordering': ['title_category_routine'],
            },
        ),
        migrations.CreateModel(
            name='Theme_goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_theme_goal', models.CharField(db_index=True, max_length=30, verbose_name='Наименование темы цели')),
            ],
            options={
                'verbose_name': 'Тема цели',
                'verbose_name_plural': 'Темы целей',
                'ordering': ['title_theme_goal'],
            },
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_routine', models.CharField(max_length=40, verbose_name='Название пункта')),
                ('text_routine', models.TextField(blank=True, max_length=300, verbose_name='Текст пункта')),
                ('with_routine', models.TimeField(blank=True, max_length=15, verbose_name='С которого время активно')),
                ('before_routine', models.TimeField(blank=True, max_length=15, verbose_name='До которого время активно')),
                ('created_at_routine', models.DateTimeField(auto_now_add=True, verbose_name='Пункт создан')),
                ('category_routine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='development.category_routine', verbose_name='Тема пунтка')),
            ],
            options={
                'verbose_name': 'Распорядок дня',
                'verbose_name_plural': 'Распорядок дня',
                'ordering': ['created_at_routine'],
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_notes', models.CharField(max_length=1000, verbose_name='Текст заметки')),
                ('created_at_notes', models.DateTimeField(auto_now_add=True, verbose_name='Создано заметка')),
                ('photo_notes', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото к заметки')),
                ('category_notes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='development.category_notes', verbose_name='Тема заметки')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['-created_at_notes'],
            },
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_goal', models.CharField(max_length=30, verbose_name='Название цели')),
                ('content_goal', models.TextField(blank=True, max_length=120, verbose_name='Текст цели')),
                ('created_at_goal', models.DateTimeField(auto_now_add=True, verbose_name='Цель создана')),
                ('theme_goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='development.theme_goal', verbose_name='Тема цели')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
                'ordering': ['-created_at_goal'],
            },
        ),
    ]