# -*- coding:UTF-8 -*-

from rest_framework import serializers
from orz_app.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("author_name", "email", "website")
