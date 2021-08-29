from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    preview = models.CharField(max_length=600)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title