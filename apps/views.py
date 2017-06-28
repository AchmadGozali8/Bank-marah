# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
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
@login_required
def Home(request):
    HIGH_LEVEL = 1
    LOW_LEVEL = 2
    NOT_DELETED = 0

    create_post = PostForm()
    posts = Post.objects.filter(deleted__exact=NOT_DELETED)
    high = posts.filter(anger_id__exact=HIGH_LEVEL).count()
    medium = posts.filter(anger_id__exact=LOW_LEVEL).count()
    count = count_level(posts)
    paginator = Paginator(posts, 5)
    page_request = "page"
    page = request.GET.get(page_request)

    try:
        posting = paginator.page(page)
    except PageNotAnInteger:
        posting = paginator.page(1)
    except EmptyPage:
        posting = paginator.page(paginator.num_pages)

    context = {
        'post': posting,
        'form': create_post,
        'page_request': page_request,
        'high': high,
        'medium': medium,
    }
    return render(request, 'timeline.html', context)


def count_level(anger):
    high = 0
    low = 0
    for p in anger:
        if p.anger_id == 1:
            high += 1
        else:
            low += 1

    context = {
        'high': high,
        'low': low,
    }
    return context


@login_required
def CreatePost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # commit = false used for
            # Create, but don't save the new form instance. 
            # because it will return an object that hasn’t yet been saved to the database
            print "file yang di upload", request.FILES
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    context = {
        "form": form,
    }
    return redirect('/', context)


def UpdatePost(request, pk):
    # raise exception if None and get pk if exists
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # form.user = request.user
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

        if form:
            form.fields['description'].widget.attrs['placeholder'] = post.description

    context = {
        "form": form,
        "pk" : pk,
    }

    return render(request, 'update.html', context)


def DeletePost(request, pk):
    DELETED = 1
    NOT_DELETED = 0
    response_data = {}

    post = get_object_or_404(Post, id=pk)
    #    deleteStatus = Post.objects.get(id=pk)

    if post.deleted == NOT_DELETED:
        post.deleted = DELETED
        response_data['status'] = "Deleted"
    else:
        post.deleted = NOT_DELETED
        response_data['status'] = "Not Deleted"

    post.save()
    # return HttpResponse(json.dumps(response_data),
    #                     content_type="application/json")
    return HttpResponseRedirect('/') 
