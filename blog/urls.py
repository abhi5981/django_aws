from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('blog7', views.blog7, name='blog7'),
]