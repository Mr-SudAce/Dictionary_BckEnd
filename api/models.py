from django.db import models
from tinymce.models import HTMLField

# Create your models here.




class WordModel(models.Model):
    word = models.CharField(max_length=100, default="", unique=True)
    antonyms = models.CharField(max_length=100, default="")
    synonyms = models.CharField(max_length=100, default="")
    example = models.CharField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    description = HTMLField()
    
    def __str__(self):
        return self.word

class PostModel(models.Model):
    title = models.CharField(max_length=100, default="", unique=True)
    image = models.ImageField(upload_to="images/", blank=True)
    # description = models.CharField(max_length=100, default="")
    full_desc = HTMLField()
    
    def __str__(self):
        return self.title

class FooterModel(models.Model):
    heading = models.CharField(max_length=50)
    description = HTMLField()
    
    def __str__(self):
        return self.heading