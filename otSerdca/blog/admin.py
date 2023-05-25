from django.contrib import admin
from .models import Gallery, Photo

# Register your models here.


class PhotoTabularInline(admin.StackedInline):
    model = Photo


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoTabularInline]

    class Meta:
        model = Gallery


admin.site.register(Gallery, GalleryAdmin)
