from django.db import models
from .models import *
from tinymce.models import HTMLField
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import AbstractUser,Group, Permission
# from .models import CustomUser
# from django.contrib.auth.decorators import admin



class WordModel(models.Model):
    word = models.CharField(max_length=100, unique=True, default="")
    antonyms = models.CharField(max_length=100, default="", blank=True)
    synonyms = models.CharField(max_length=100, default="", blank=True)
    example = models.CharField(max_length=500, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = HTMLField()

    def __str__(self):
        return self.word

class PostCategoryModel(models.Model):
    cat_order = models.IntegerField(default=0, unique=True)
    cat_title = models.CharField(max_length=100, unique=True, default="")
    def __str__(self):
        return self.cat_title

class PostModel(models.Model):
    title = models.CharField(max_length=100, unique=True, default="")
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

class PageModel(models.Model):
    page_title = models.CharField(max_length=100, unique=True, default="")
    page_description = HTMLField()
    
    def __str__(self):
        return self.page_title

class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100, unique=True, default="")
    blog_description = HTMLField()
    blog_image = models.ImageField(upload_to="images/")
    blog_author = models.CharField(max_length=100, default="")
    post_Cat = models.ForeignKey(PostCategoryModel, related_name='blogs', on_delete=models.CASCADE, default="")
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=models.functions.Now, editable=False)

    def __str__(self):
        return self.blog_title
