from django.urls import path
from .views import GalleryView, index_view, about_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_view, name='main'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('about/', about_view, name='about'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)