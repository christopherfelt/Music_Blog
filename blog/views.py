from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, View)
from django.http.response import HttpResponse
from django.http import JsonResponse
from blog.forms import PostForm
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Post_Tracks
import spotipy
import spotipy.util as util

# Create your views here.

# def get_playlist_tracks(user_id, playlist_id, model):
#     token = util.oauth2.SpotifyClientCredentials()
#     cache_token = token.get_access_token()
#     spotify = spotipy.Spotify(cache_token)
#     playlist_json = spotify.user_playlist_tracks(user=user_id, playlist_id=playlist_id, fields='tracks')
#     track_list = []
#     for track_item in playlist_json:
#         track_list.append(track_item['track']['id'])


def get_playlist(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST.copy()
            playlist_id = data.get('playlist_id')
            post_title = data.get('post_title')
            # post_author = data.get('author')
            track_list = Post_Tracks.objects.filter(post_title=post_title, playlist_id=playlist_id).values_list('track_id')
            track_list_send = []
            for track in track_list:
                track_list_send.append(track[0])

            # return JsonResponse({'tracks_to_return':list(track_list)})
            # return HttpResponse(playlist_id)

            # user = request.user
            # spotify_info = user.social_auth.get(provider='spotify')
            # spotify_id = user.username
            # token = spotify_info.extra_data['access_token']
            # spotifyObject = spotipy.Spotify(auth=token)
            # spotifyObject.user_playlist_create(user=spotify_id, name="MP_Playlist_Test2")
            # new_playlist_json = spotifyObject.current_user_playlists(limit=1)
            # new_playlist_id = new_playlist_json['items'][0]['id']
            # # track_list = ['54vEMXZQbeQ8ui3GKsKcnf', '11UK2krGqZXnr0khXrK7b6','547fOfZqXcCovdHNjywpEi']
            # spotifyObject.user_playlist_add_tracks(user=spotify_id, playlist_id=new_playlist_id, tracks=track_list_send, position=None)

            try:
                user = request.user
                spotify_info = user.social_auth.get(provider='spotify')
                spotify_id = user.username
                token = spotify_info.extra_data['access_token']
                spotifyObject = spotipy.Spotify(auth=token)
                spotifyObject.user_playlist_create(user=spotify_id, name="MP_Playlist_Test2")
                new_playlist_json = spotifyObject.current_user_playlists(limit=1)
                new_playlist_id = new_playlist_json['items'][0]['id']
                # track_list = ['54vEMXZQbeQ8ui3GKsKcnf', '11UK2krGqZXnr0khXrK7b6','547fOfZqXcCovdHNjywpEi']
                spotifyObject.user_playlist_add_tracks(user=spotify_id, playlist_id=new_playlist_id, tracks=track_list_send, position=None)
                return HttpResponse('Playlist Add Successful')
            except:
                return HttpResponse('Playlist Add Failed')
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
    def form_valid(self, form):
        self.object = form.save()
        user_id = form.cleaned_data['user_id']
        playlist_id = form.cleaned_data['playlist_id']
        post_title = form.cleaned_data['title']
        author = form.cleaned_data['author']
        token = util.oauth2.SpotifyClientCredentials()
        cache_token = token.get_access_token()
        spotify = spotipy.Spotify(cache_token)
        playlist_json = spotify.user_playlist_tracks(user=user_id, playlist_id=playlist_id, fields='items(track(id))')
        track_number=1
        for track_item in playlist_json['items']:
            record = Post_Tracks()
            record.playlist_id = playlist_id
            record.track_number = track_number
            track_number = track_number+1
            record.post_title = post_title
            record.track_id = track_item['track']['id']
            record.post_author = author
            record.save()
        return super().form_valid(form)












