# -*- coding:UTF-8 -*-

from django.shortcuts import redirect, render_to_response
from .forms import CommentForms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from markdown import markdown
from models import *
from utils import *


def index(request):
    all_article = Article.objects.all().order_by('-publish_time')
    classifications = Classification.objects.all()
    hot_articles = Article.objects.all().order_by('-counts')[:5]
    for article in all_article:
        article.context = markdown(article.context, ['codehilite'])
    paginator = Paginator(all_article, 5, 1)
    page = request.GET.get('page')
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {"classifications": classifications,
                                             "hot_articles": hot_articles,
                                             "articles": article})


def article_detail(request, id):
    #当前id的文章具体内容
    article_all_detail = Article.objects.get(id=int(id))
    # 阅读量+1
    article_all_detail.add_counts()
    #当前id的文章前10条评论
    blog_comments = Comment.objects.filter(article_id=int(id)).order_by('-created_time')[:10]
    #文章高亮
    article_all_detail.context = markdown(article_all_detail.context, ['codehilite'])
    #获取当前id的上一篇文章和下一篇文章
    pre_articles = Article.objects.filter(id__lt=int(id)).order_by('-publish_time')[:1]
    next_articles = Article.objects.filter(id__gt=int(id)).order_by('publish_time')[:1]

    return render_to_response("article_detail.html",
                              {'context': article_all_detail,
                               "blog_comments": blog_comments,
                               "pre_articles": pre_articles,
                               "next_articles": next_articles
                               })


def comment_post(request, article_id):
    article = Article.objects.get(id=article_id)
    comment_form = CommentForms(request.POST)
    comment = Comment.objects.create(
        user_name=deal_post_comments_str(comment_form["user_name"]),
        user_email=deal_post_comments_str(comment_form["user_email"]),
        blog_comment=deal_post_blog_comments_str(comment_form["blog_comment"]),
        article_id=article
    )
    comment.save()
    return redirect(request.META['HTTP_REFERER'])


def show_classification(request, classification):
    classifica = Classification.objects.get(english_name=classification)
    classification_id = classifica.id
    all_article = Article.objects.filter(classification=int(classification_id)).order_by('-publish_time')
    hot_articles = Article.objects.filter(classification=int(classification_id)).order_by('-counts')[:5]
    classifications = Classification.objects.all()
    for article in all_article:
        article.context = markdown(article.context, ['codehilite'])
    paginator = Paginator(all_article, 5, 1)
    page = request.GET.get('page')
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {"classifications": classifications,
                                             "hot_articles": hot_articles,
                                             'articles': article})


# Create your views here.
