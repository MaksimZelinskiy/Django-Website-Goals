from django import template
from django.db.models import *

from journal.models import Article
register = template.Library()

@register.inclusion_tag('journal/article_last3.html')
def article_last():
    article = Article.objects.all()
    return { 
        "article": article,
    }