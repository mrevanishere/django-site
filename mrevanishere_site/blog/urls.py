from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article, name='article'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]