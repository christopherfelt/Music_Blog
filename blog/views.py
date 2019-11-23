from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, View)
from django.http.response import HttpResponse
from blog.forms import PostForm
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
import spotipy

# Create your views here.

def get_playlist(request):
    if request.user.is_authenticated:
        # try:
        user = request.user
        spotify_info = user.social_auth.get(provider='spotify')
        spotify_id = user.username
        token = spotify_info.extra_data['access_token']
        spotifyObject = spotipy.Spotify(auth=token)
        spotifyObject.user_playlist_create(user=spotify_id, name="MP_Playlist_Test1")
        new_playlist_json = spotifyObject.current_user_playlists(limit=1)
        new_playlist_id = new_playlist_json['items'][0]['id']
        track_list = ['54vEMXZQbeQ8ui3GKsKcnf', '11UK2krGqZXnr0khXrK7b6','547fOfZqXcCovdHNjywpEi']
        spotifyObject.user_playlist_add_tracks(user=spotify_id, playlist_id=new_playlist_id, tracks=track_list, position=None)
        return HttpResponse('Playlist Add Successful')
        # except:
        #     return HttpResponse('Playlist Add Failed')
    else:
        return HttpResponse('Something Wrong With User')




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









