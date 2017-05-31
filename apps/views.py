# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .forms import PostForm, PostUpdateForm
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# Class based views

# class Posts(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'form.html'
#     success_url = 'index.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(Posts, self).form_valid(form)


# class PostsUpdate(LoginRequiredMixin, UpdateView):
#     model = Post
#     form_class = PostUpdateForm
#     template_name = "posts_update_form.html"
#     success_url = '/test/'

# #FUNCTIONAL BASED VIEWS
def Posts(request):
    create_post = PostForm()
    posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page_request = "page"
    page = request.GET.get(page_request)
    
    try:
        posting = paginator.page(page)
    except PageNotAnInteger:
        posting = paginator.page(1)
    except EmptyPage:
        posting= paginator.page(paginator.num_pages)

    context = {
        'post':posting,
        'form':create_post,
        'page_request':page_request
    }
    
    return render(request, 'home.html', context)


def CreatePost(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # commit = false used for
            # Create, but don't save the new form instance. 
            # because it will return an object that hasn’t yet been saved to the database
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/post/')
    else:
        form = PostForm()
    return render(request, 'home.html', {'form': form})


def UpdatePost(request, pk):
    #raise exception if None and get pk if exists
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            #form.user = request.user
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = PostUpdateForm()
    return render(request, 'posts_update_form.html', {'form':form})


def DeletePost(request, pk):
    DELETED = 1
    NOT_DELETED = 0
    response_data =  {}

    post = get_object_or_404(Post, id=pk)
    #deleteStatus = Post.objects.get(id=pk)
    
    if post.deleted == NOT_DELETED:
        post.deleted = DELETED
        response_data['status'] = "Deleted"
    else:
        post.deleted = NOT_DELETED
        response_data['status'] = "Not Deleted"

    post.save()
    return HttpResponse(json.dumps(response_data), content_type="application/json")

