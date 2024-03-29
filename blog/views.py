# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils import timezone
from .models import Post
from django.shortcuts import render


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


