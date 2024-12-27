from django.db import models
from tinymce.models import HTMLField

# Models for Word, Posts, Categories, Footer, and Header


class WordModel(models.Model):
    word = models.CharField(max_length=100, default="")
    antonyms = models.CharField(max_length=100, default="", blank=True)
    synonyms = models.CharField(max_length=100, default="", blank=True)
    example = models.CharField(max_length=500, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = HTMLField()

    def __str__(self):
        return self.word


class PostCategoryModel(models.Model):
    cat_title = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.cat_title


class PostModel(models.Model):
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="images/", blank=True)
    full_desc = HTMLField()
    postCat = models.ForeignKey(
        PostCategoryModel, 
        related_name="posts", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class FooterModel(models.Model):
    heading = models.CharField(max_length=50, unique=True)
    description = HTMLField()

    def __str__(self):
        return self.heading


class HeaderModel(models.Model):
    site_title = models.CharField(max_length=100, default="")
    logo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.site_title
