# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAmdin(admin.ModelAdmin):
    list_display = ['__unicode__', 'update', 'timestamp']
    # list_display_links = ['update']
    list_filter = ['update', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAmdin)