from django.db import models

# Create your models here.




class WordModel(models.Model):
    word = models.CharField(max_length=100, default="", unique=True)
    description = models.TextField(default="")
    antonyms = models.CharField(max_length=100, default="")
    synonyms = models.CharField(max_length=100, default="")
    example = models.CharField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word


class PostModel(models.Model):
    title = models.CharField(max_length=100, default="", unique=True)
    image = models.ImageField(upload_to="images/", blank=True)
    description = models.CharField(max_length=100, default="") 
    full_desc = models.TextField(default="")
    
    def __str__(self):
        return self.title