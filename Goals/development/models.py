from django.db import models
from django.shortcuts import render
from django.urls import reverse




#    GOALS    #
class Goals (models.Model):
    title_goal= models.CharField(max_length=30, verbose_name='Название цели')
    content_goal= models.TextField(blank=True, verbose_name='Текст цели', max_length=120)
    created_at_goal= models.DateTimeField(auto_now_add=True, verbose_name='Цель создана')
    theme_goal= models.ForeignKey('Theme_goal', on_delete=models.PROTECT, null=True, verbose_name='Тема цели')

    def get_delete_goal(self):
        return reverse ("deletegoals", kwargs={"pk": self.pk})

    def get_update_goals(self):
        return reverse ("edit_goal", kwargs={"pk": self.pk})


    def __str__(self):
        return self.title_goal

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'
        ordering = ['-created_at_goal']

class Theme_goal(models.Model):
    title_theme_goal = models.CharField(max_length=30, db_index=True, verbose_name='Наименование темы цели')

    def get_url(self):
        return reverse('theme_goal', kwargs={ "theme_goal_id": self.pk })

    def __str__(self):
        return self.title_theme_goal

    class Meta:
        verbose_name = 'Тема цели'
        verbose_name_plural = 'Темы целей'
        ordering = ['title_theme_goal']




#    NOTES    #
class Notes(models.Model):
    title_notes =models.CharField(max_length=100, verbose_name="Название" , blank=True)
    content_notes = models.TextField(max_length=1000, verbose_name='Текст', blank=True)
    created_at_notes=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    photo_notes = models.ImageField(upload_to = 'photos/%Y/%m/%d/',  verbose_name='Фото', blank=True)
    category_notes=models.ForeignKey('Category_notes', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_delete_notes(self):
        return reverse ("deletenotes", kwargs={"pk": self.pk})

    def get_update_notes(self):
        return reverse ("edit_notes", kwargs={"pk": self.pk})


    def __str__(self):
        return self.content_notes

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at_notes']

class Category_notes(models.Model):
    title_category_notes = models.CharField(max_length=30, db_index=True, verbose_name='Наименование категории заметки')

    def get_notes_url(self):
        return reverse('category_notes', kwargs={ "category_notes_id": self.pk })


    def __str__(self):
        return self.title_category_notes

    class Meta:
        verbose_name = 'Категория заметки'
        verbose_name_plural = 'Категории заметок'
        ordering = ['title_category_notes']




#    Routine    #
class Routine(models.Model):
    title_routine=models.CharField(max_length=40, verbose_name='Название пункта')
    text_routine=models.TextField(blank=True, verbose_name='Текст пункта', max_length=300)
    with_routine=models.TimeField(max_length=15,blank=True, verbose_name="С которого время активно")
    before_routine=models.TimeField(max_length=15,blank=True, verbose_name="До которого время активно")
    created_at_routine=models.DateTimeField(auto_now_add=True,verbose_name="Пункт создан")
    category_routine=models.ForeignKey('Category_routine', on_delete=models.PROTECT, null=True, verbose_name='Тема пунтка')

    def get_delete_routine(self):
        return reverse ("deleteroutine", kwargs={"pk": self.pk})

    def get_update_routine(self):
        return reverse ("edit_routine", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title_routine

    class Meta:
        verbose_name = 'Распорядок дня'
        verbose_name_plural = 'Распорядок дня'
        ordering = ['created_at_routine']

class Category_routine(models.Model):
    title_category_routine=models.CharField(max_length=30, db_index=True, verbose_name='Наименование категории распорядка')

    def get_routine_url(self):
        return reverse('category_routine', kwargs={ "category_routine_id": self.pk })

    def __str__(self):
        return self.title_category_routine

    class Meta:
        verbose_name = 'Категория распорядка'
        verbose_name_plural = 'Категории распорядка'
        ordering = ['title_category_routine']

