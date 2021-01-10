from django import forms
from ckeditor.fields import CKEditorWidget
from django.contrib import admin
from django.db import models
from blog.models import BlogPost


class InputForm(forms.ModelForm):
    """
    Update blogpost form
    """
    # title = forms.CharField(max_length=200)
    # sub_title = forms.CharField(max_length=500)
    # article = CKEditorWidget()
    class Meta:
        model = BlogPost
        fields = ('title', 'preview', 'body', 'pub_date', 'mod_date')
