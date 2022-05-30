from django.urls import path

from .views import *

urlpatterns = [
    path('', Journal, name='journal'),
    path('article', ArticleViews.as_view(), name='article'),
    path('article/<int:pk>', Content_article.as_view() , name='content_article'),
    path('book_review', Book_review.as_view(), name='book_review')
]

