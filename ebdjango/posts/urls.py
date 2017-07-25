"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_home,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [

    url(r'^$', post_home, name="posts"),
    url(r'^create/$', post_create, name="create"),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^update/$', post_update, name="update"),
    url(r'^delete/$', post_delete, name="delete"),

    # url(r'^posts/$', "<appname>.views.<function_name>"), directly call url
]
