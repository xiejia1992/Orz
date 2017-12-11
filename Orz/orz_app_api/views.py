# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from orz_app.models import Author, Article
from .serializer import AuthorSerializer, ArticleSerializer
from .api_method_utils import get_model_list, add_model, get_model_id, put_model_id, delete_model_id


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        return get_model_list(request=request,
                              Model=Author,
                              Serializer=AuthorSerializer)
    elif request.method == 'POST':
        return add_model(request=request,
                         Model=Author,
                         Serializer=AuthorSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, id):
    if request.method == 'GET':
        return get_model_id(request=request,
                            id=id,
                            Model=Author,
                            Serializer=AuthorSerializer)
    elif request.method == 'PUT':
        return put_model_id(request=request,
                            id=id, Model=Author,
                            Serializer=AuthorSerializer)
    elif request.method == 'DELETE':
        return delete_model_id(request=request,
                               id=id,
                               Model=Author)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        return get_model_list(request=request,
                              Model=Article,
                              Serializer=ArticleSerializer)
    elif request.method == 'POST':
        return add_model(request=request,
                         Model=Article,
                         Serializer=ArticleSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    if request.method == 'GET':
        return get_model_id(request=request,
                            id=id,
                            Model=Article,
                            Serializer=ArticleSerializer)
    elif request.method == 'PUT':
        return put_model_id(request=request,
                            id=id, Model=Article,
                            Serializer=ArticleSerializer)
    elif request.method == 'DELETE':
        return delete_model_id(request=request,
                               id=id,
                               Model=Article)

# Create your views here.
