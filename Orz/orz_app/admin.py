# -*- coding:UTF-8 -*-

from django.contrib import admin
from .models import Article, Author, Classification, Tag


admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Classification)
admin.site.register(Tag)

# Register your models here.
