# -*- coding:UTF-8 -*-

from __future__ import unicode_literals
from django.db import models


class Tag(models.Model):
    ''' 定义标签模型 '''
    tag_name = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


class Classification(models.Model):
    ''' 定义类别模型 '''
    classifiication_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.classifiication_name


class Author(models.Model):
    ''' 定义作者模型 '''
    author_name = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.author_name


class Article(models.Model):
    ''' 定义文章模型 '''
    caption = models.CharField(max_length=64)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author)
    classification = models.ForeignKey(Classification)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.caption


# Create your models here.
