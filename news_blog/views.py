from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Article, Author, Comment


def index(request):
    articles = Article.objects.all()
    return render(request, 'news_blog/news_list.html', {'articles': articles})


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        author = Author.objects.filter(article__pk=article_id)
        comments = Comment.objects.filter(article__pk=article_id)
    except (Article.DoesNotExist, Author.DoesNotExist, Comment.DoesNotExist) as error:
        return HttpResponseNotFound(error)
    return render(request, 'news_blog/news_article.html',
                  {'article': article,
                   'author': author,
                   'comments': comments
                   }
                  )


def show_about(request):
    return render(request, 'news_blog/about.html')
