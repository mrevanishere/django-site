from django.contrib import admin

# Register your models here.
from .models import BlogPost

# Gives access to django admin form for BlogPost
admin.site.register(BlogPost)