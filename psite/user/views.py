from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import InputForm
from blog.models import BlogPost


def dashboard(request) -> HttpResponse:
    print(request)
    context = {'form': InputForm()}
    return render(request, 'user/dashboard.html', context)


def post_article(request, *args, **kwargs) -> HttpResponse:
    """
    Called when the form action="/account/post_article" activates.
    Saves the form data to the database by creating a new BlogPost.
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    print(request.body)
    print(args)
    print(kwargs)
    pk = kwargs.get('pk')
    bp_instance = get_object_or_404(BlogPost)
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            bp_instance = BlogPost.objects.create(
                title = form.cleaned_data['title'],
                pub_date=form.cleaned_data['pub_date'],
                mod_date=form.cleaned_data['mod_date'],
                preview=form.cleaned_data['preview'],
                body=form.cleaned_data['body'],
            )

            """
            These can be used to edit a current object
            """
            # bp_instance.title = form.cleaned_data['title']
            # bp_instance.pub_date = form.cleaned_data['pub_date']
            # bp_instance.mod_date = form.cleaned_data['mod_date']
            # bp_instance.preview = form.cleaned_data['preview']
            # bp_instance.body = form.cleaned_data['body']
            bp_instance.save()
            print(bp_instance)

            # return HttpResponseRedirect('/')



    # context = {'form': InputForm()}
    # return render(request, "user/dashboard.html", context)
