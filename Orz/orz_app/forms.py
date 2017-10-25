# -*- coding:UTF-8 -*-

from django import forms
from .models import Article, Comment


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'user_email', 'blog_comment')
        widgets = {
            'user_name': forms.TextInput(),
            'user_email': forms.TextInput(),
            'blog_comment': forms.Textarea(),
        }

    def is_vaild(self):
        pass