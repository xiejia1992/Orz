# -*- coding:UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from markdown import markdown
from models import *


def index(request):
    all_article = Article.objects.all().order_by('-publish_time')
    for article in all_article:
        article.context = markdown(article.context, ['codehilite'])
    paginator = Paginator(all_article, 5, 1)
    page = request.GET.get('page')
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'articles': article})


def article_detail(request, id):
    article_all_detail = Article.objects.get(id=int(id))
    article_all_detail.context = markdown(article_all_detail.context, ['codehilite'])
    return render_to_response("article_detail.html", {'context': article_all_detail})


# Create your views here.
