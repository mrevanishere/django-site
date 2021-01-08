from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def index(request):
    latest_posts = BlogPost.objects.order_by('-pub_date')[:10]
    context = {
        'latest_posts': latest_posts,
    }
    # return HttpResponse("Index of Blog")
    return render(request, 'blog/index.html', context)


def article(request, id):
    try:
        post = get_object_or_404(BlogPost, pk=id)
    except BlogPost.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/article.html', {'post': post})


def contact(request):
    return render(request, 'blog/contact.html')


def login(request):
    return render(request, 'blog/login.html')