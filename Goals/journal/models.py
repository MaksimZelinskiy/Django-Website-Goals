from django.db import models
from django.urls import reverse


# *************
# Model Article
# *************

class Article(models.Model):
    title_article=models.CharField(max_length=100, verbose_name='Название статьи')
    content_article=models.TextField(blank=True, verbose_name='Текст статьи', max_length=10000)
    created_at_article=models.DateTimeField(auto_now_add=True, verbose_name='Статья создана')
    photo_article=models.ImageField(upload_to = 'photos/%Y/%m/%d/',  verbose_name='Фото статьи')
    is_published_article=models.BooleanField(default=True, verbose_name='Публиковать статью')
    theme_article=models.ForeignKey('Theme_article', on_delete=models.PROTECT, null=True, verbose_name='Тема статьи')
    views_article =models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('content_article', kwargs={ "pk": self.pk })

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering=['-created_at_article']

class Theme_article(models.Model):
    title_theme_article=models.CharField(max_length=150, db_index=True, verbose_name='Наименование темы статьи')

    def __str__(self):
        return self.title_theme_article

    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статей'
        ordering=['title_theme_article']




# *************
# Model Book review
# *************

class Book_review(models.Model):
    title_review = models.CharField(max_length=100, verbose_name='Название книги для обзора')
    text_review = models.TextField(blank=True, verbose_name='Текст обзора книги', max_length=10000)
    author_review= models.CharField(max_length=30, verbose_name='Автор книги с обзора')
    created_at_review=models.DateTimeField(auto_now_add=True, verbose_name='Обзор книги создан')
    photo_review=models.ImageField(upload_to = 'photos/%Y/%m/%d/',  verbose_name='Фото книги с обзора')
    theme_review=models.ForeignKey('Theme_review_book', on_delete=models.PROTECT, null=True, verbose_name='Тема книги с обзора')


    def __str__(self):
        return self.title_review

    class Meta:
        verbose_name = 'Обзор книги'
        verbose_name_plural = 'Обзоры книг'
        ordering=['-created_at_review']

class Theme_review_book(models.Model):
    title_theme_review=models.CharField(max_length=150, db_index=True, verbose_name='Наименование темы обзора на книг')

    def __str__(self):
        return self.title_theme_review

    class Meta:
        verbose_name = 'Тема обзора на книг'
        verbose_name_plural = 'Тема обзора на книг'
        ordering=['title_theme_review']


