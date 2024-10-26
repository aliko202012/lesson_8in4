from django.shortcuts import render
from apps.main.models import Main, Event, Artist,Blog
# Create your views here.

def main(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html', locals())


def artist(request):
    artist = Artist.objects.all()
    return render(request, 'artist.html', locals())


def event(request):
    event = Event.objects.latest('id')
    return render(request, 'event-list-3.html', locals())

def event_detail(request, id):
    event_detail = Event.objects.get(id=id)
    return render(request, 'event-detail.html', locals())

def blog(request):
    blog = Blog.objects.latest('id')
    return render(request, 'blog-small.html', locals())

def blog_detail(request,id):
    blog_detail = Blog.objects.get(id=id) 
    return render(request,'blog-detail.html', locals())