from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class pandastutorial(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, default=None)
    content = RichTextField()
    meta_tags = models.TextField(max_length=1000, default=None)
    meta_description = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("pandas:pandascontent", args=[self.id])
    