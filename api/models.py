from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=100, default="", unique=True)
    description = models.CharField(max_length=500, default="")
    antonyms = models.CharField(max_length=100, default="")
    synonyms = models.CharField(max_length=100, default="")
    example = models.CharField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word