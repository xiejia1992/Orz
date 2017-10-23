# -*- coding:UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import *


def index(request):
    all_article = Article.objects.all().order_by('-publish_time')
    return render_to_response('index.html', {'all_article': all_article})


def article_detail(request, id):
    article_all_detail = Article.objects.get(id=int(id))
    return render_to_response("article_detail.html", {'context': article_all_detail})


# Create your views here.
