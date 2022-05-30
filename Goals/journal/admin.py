from django.contrib import admin

from .models import Article, Theme_article, Book_review, Theme_review_book

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_article', 'created_at_article','theme_article')
    list_display_links=('id', 'title_article')
    search_fields = ('title_article', 'content_article','theme_article')

class Theme_articleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_theme_article')
    list_display_links=('id', 'title_theme_article')



class Book_reviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_review', 'created_at_review','theme_review')
    list_display_links=('id', 'title_review')
    search_fields = ('title_review', 'text_review','theme_review')

class Theme_review_bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_theme_review')
    list_display_links=('id', 'title_theme_review')




admin.site.register(Article, ArticleAdmin)
admin.site.register(Theme_article, Theme_articleAdmin)

admin.site.register(Book_review, Book_reviewAdmin)
admin.site.register(Theme_review_book, Theme_review_bookAdmin)


