from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('personal-finance', views.personalfinance, name='personal-finance'),
]