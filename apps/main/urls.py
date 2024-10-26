from django.urls import path
from apps.main.views import main, artist, event, event_detail, blog, blog_detail

urlpatterns = [
    path('', main, name='main'),
    path('artist/', artist, name='artist'),
    path('event/', event, name='event'),
    path('event_detail/<int:id>/', event_detail, name='event_detail'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:id>/', blog_detail, name='blog_detail'),
]
