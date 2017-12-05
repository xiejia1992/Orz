# -*- coding: utf-8 -*-

import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orz_app.models import Author
from .serializer import AuthorSerializer


@api_view(['GET', 'POST'])
def authors_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = u'禁止添加'
        return Response(data, status=status.HTTP_403_FORBIDDEN)

#    elif request.method == 'POST':
#        serializer = AuthorSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = u'禁止更新'
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    elif request.method == "DELETE":
        data = u'禁止删除'
        return Response(data, status=status.HTTP_403_FORBIDDEN)

#    elif request.method == "PUT":
#        serializer = AuthorSerializer(author, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == "DELETE":
#        author.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
