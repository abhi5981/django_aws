from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')

def personalfinance(request):
    return render(request, 'blog/personal-finance.html')
