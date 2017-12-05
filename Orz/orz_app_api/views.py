# -*- coding: utf-8 -*-

import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orz_app.models import Author
from .serializer import AuthorSerializer


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print request.data
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
