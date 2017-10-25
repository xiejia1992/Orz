# -*- coding:UTF-8 -*-

from django.contrib import admin
from .models import Article, Author, Classification, Tag, Comment


admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Comment)

# Register your models here.
