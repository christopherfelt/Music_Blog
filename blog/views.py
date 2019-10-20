from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, CreateView, ListView, DetailView)
from blog.forms import PostForm
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = "home.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter().order_by('-published_date')[:1]

class LibraryPageView(ListView):
    template_name = "library.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter().order_by('published_date')


class BlogPageView(DetailView):
    template_name = "blog_detail.html"
    model = Post

class AboutPageView(TemplateView):
    template_name = "about.html"

# class ContactPageView(TemplateView):
#     template_name = "static/discard/contact.html"

# class DraftPostView(TemplateView):
#     template_name = "static/discard/draft.html"
#     login_url = '/login/'
#     redirect_field_name = 'homepage.html'
#     form_class = PostForm
#     model = Post

class CreatePostView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_form.html'
    success_url = reverse_lazy('homepage')





