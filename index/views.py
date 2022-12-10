from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')


def projects(request):
    return render(request, 'index/projects.html')


def nameless(request):
    return render(request, 'index/nameless.html')
