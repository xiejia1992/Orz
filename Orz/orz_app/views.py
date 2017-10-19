# -*- coding:UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"第一个博客")

# Create your views here.
