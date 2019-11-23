from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    playlist_id = models.CharField(max_length=255, default="7qP3wKi5ynkAUw7Jlmwj7v")
    # spotify: playlist:7qP3wKi5ynkAUw7Jlmwj7v
    # post_image = models.ImageField(upload_to='', default='none.png')


    def get_absolute_url(self):
        return reverse("homepage")

    def __str__(self):
        return self.title


