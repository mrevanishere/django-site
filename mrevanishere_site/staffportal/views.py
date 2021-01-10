from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import InputForm
from blog.models import BlogPost


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        render(request, '')
    else:
        render(request, 'blog/index.html')


def dash_post(request):
    context = {'form': InputForm()}
    return render(request, 'staffportal/dashboard.html', context)


def submit_post(request, *args, **kwargs):
    """
    Called when the form action="/account/submit_post" activates.
    Saves the form data to the database by creaitng a new BlogPost.
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    # pk = kwargs.get('pk')
    # bp_instance = get_object_or_404(BlogPost)
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
            # bp_instance.save()
            # print(bp_instance)

            return HttpResponseRedirect('/')
    else:
        pass

    context = {'form': InputForm()}
    return render(request, "staffportal/dashboard.html", context)
