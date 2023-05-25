from django.db import models

# Create your models here.


class Gallery(models.Model):
    title = models.TextField(max_length=300)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class Photo(models.Model):
    photo = models.ImageField(upload_to='static/blog')
    galleryRelated = models.ForeignKey(Gallery, on_delete=models.CASCADE)


    
    
    
