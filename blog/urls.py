from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static, serve

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('blog/<int:pk>/', views.BlogPageView.as_view(), name='blogpage'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    # path('contact/', views.ContactPageView.as_view(), name='contact'),
    # path('accounts/login/draft/', views.DraftPostView.as_view(), name='draft'),
    path('accounts/login/new/', views.CreatePostView.as_view(), name='createpost'),
    path('library/', views.LibraryPageView.as_view(), name='library'),
    path('add_playlist/', views.get_playlist, name='get_playlist'),
    path('user_blog_detail/<int:pk>', views.BlogPostDetail.as_view(), name='user_detail'),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)