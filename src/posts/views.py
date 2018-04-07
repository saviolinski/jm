# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post
from .forms import PostForm
# Create your views here.
def posts_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		return	HttpResponseRedirect("/admin/login/?next=/create/")	
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return	HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def posts_detail(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	context = {
		"post": instance
	}
	return render(request, "detail.html", context)

def posts_list(request):
	queryset = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
						Q(title__icontains=query) |
						Q(content__icontains=query)	
						).distinct()
	context = {
		"object_list": queryset
	}
	return render(request, "post_list.html", context)

def index(request):
	queryset_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
						Q(title__icontains=query) |
						Q(content__icontains=query)	
						).distinct()
	page_template = 'post_list.html'
	template = 'index.html'
	context = {
	        'object_list': queryset_list,
	        'page_template': page_template,
	    }
	if request.is_ajax():
	    template = page_template
	return render(request, template, context)






	# queryset_list = Post.objects.all() #.order_by("-timestamp")

	# paginator = Paginator(queryset_list, 3)
	# page_request_var = "page"
	# page = request.GET.get(page_request_var)
	# try:
	# 	queryset = paginator.page(page)
	# except PageNotAnInteger:
 #        # If page is not an integer, deliver first page.
	# 	queryset = paginator.page(1)
	# except EmptyPage:
 #        # If page is out of range (e.g. 9999), deliver last page of results.
	# 	queryset = paginator.page(paginator.num_pages)

	# context = {
	# 	"object_list": queryset,
	# 	"page_request_var": page_request_var
	# }
	# return render(request, "index.html", context)




def posts_update(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, instance=instance)
	if not request.user.is_staff or not request.user.is_superuser:
		return	HttpResponseRedirect("/admin/login/?next=/update/%s")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return	HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
		"post": instance
	}
	return render(request, "post_form.html", context)

def posts_delete(request, slug):
	if not request.user.is_staff or not request.user.is_superuser:
		return	HttpResponseRedirect("/admin/login/?next=/delete/")
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	return redirect("posts:list")