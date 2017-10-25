# -*- coding:UTF-8 -*-
#添加共用函数


def deal_post_comments_str(post_data):
    data = str(post_data).split()[3]
    v = str(data).split('"')[1]
    return v


def deal_post_blog_comments_str(post_data):
    data = str(post_data).replace('\n', '>').split('>')[2]
    v = str(data).split('<')[0]
    return v