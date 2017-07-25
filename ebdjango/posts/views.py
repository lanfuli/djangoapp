# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def post_home(request):
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My user list"
    # }
    # #     here you can use different render to show different html page return render(request, "index.html", context)
    # else:
    #     context = {
    #         "title": "General list"
    #     }
    # return render(request, "index.html", context)
    queryset = Post.objects.all()
    context = {
        "query_list": queryset,
        "title": "General list"
        }
    return render(request, "index.html", context)

def post_create(request):
    return HttpResponse("<h1>Create</h1>")
def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
        }
    return render(request, "post_detail.html", context)
def post_update(request):
    return HttpResponse("<h1>update</h1>")
def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

