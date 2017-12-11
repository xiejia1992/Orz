# -*- coding:UTF-8 -*-

from rest_framework import serializers
from orz_app.models import Author, Tag, Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "author_name", "email", "website")


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id",
                  "caption",
                  "publish_time",
                  "update_time",
                  "author",
                  "classification",
                  "tags",
                  "image_name",
                  "counts")