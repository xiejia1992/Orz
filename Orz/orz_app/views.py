# -*- coding:UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import *


def index(request):
    all_article = Article.objects.all()
    return render_to_response('index.html', {'all_article': all_article})

# Create your views here.
