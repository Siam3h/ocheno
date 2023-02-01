from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.conf import settings


def error_404_view(request, exception):
	return render(request, 'blog/404.html')

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 2

class PostDetailView(DetailView):
	model = Post








