from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Article, Book_review
from .models import Article as ArticleModel



# *************
# MODEL Article
# *************

class ArticleViews(ListView):
    model=Article
    template_name= 'journal/article.html'
    context_object_name= 'article'

    
class Content_article(DetailView):
    model = Article
    context_object_name = "content_article"

# *************



# *************
# MODEL Book Review
# *************
class Book_review(ListView):
    model= Book_review
    template_name= 'journal/book_review.html'
    context_object_name='book_review'

# *************




# *************
# MODEL Main Page Journal
# *************
def Journal(request):
    context={}
    return render(request, 'journal/journal.html', context)

# *************

