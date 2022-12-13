from django.http import HttpResponse
from django.shortcuts import render
from .models import Projects


def index(request):
    return render(request, 'index/index.html')


def projects(request):
    all_project = Projects.objects.all()
    return render(request, 'index/projects.html', {'all_project': all_project})


def nameless(request):
    return render(request, 'index/nameless.html')


def detail(request, post_id):
    project = Projects.objects.get(pk=post_id)
    return render(request, 'index/detail.html', {'id': post_id, 'project': project})
