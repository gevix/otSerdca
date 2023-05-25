from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Gallery, Photo


class GalleryView(ListView):
    model = Gallery
    template_name = 'blog/gallery.html'

def index_view(request):
    return render(request, 'blog/index.html', {})

def about_view(request):
    return render(request, 'blog/about.html')
