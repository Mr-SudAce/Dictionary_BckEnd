from django.db import models
from tinymce.models import HTMLField

# models for the dictionary app



class WordModel(models.Model):
    word = models.CharField(max_length=100, unique=True, db_index=True)
    antonyms = models.CharField(max_length=100, blank=True)
    synonyms = models.CharField(max_length=100, blank=True)
    example = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = HTMLField()

    def __str__(self):
        return self.word

class PostCategoryModel(models.Model):
    cat_order = models.IntegerField(default=0, unique=True, db_index=True)
    cat_title = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.cat_title

class PostModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/", blank=True)
    full_desc = HTMLField()
    postCat = models.ForeignKey(
        PostCategoryModel,
        related_name="posts",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

class FooterModel(models.Model):
    heading = models.CharField(max_length=50, unique=True)
    description = HTMLField()

    def __str__(self):
        return self.heading

class HeaderModel(models.Model):
    site_title = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.site_title

class PageModel(models.Model):
    page_title = models.CharField(max_length=100, unique=True)
    page_description = HTMLField()

    def __str__(self):
        return self.page_title

class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100, unique=True)
    blog_description = HTMLField()
    blog_image = models.ImageField(upload_to="images/")
    blog_author = models.CharField(max_length=100, blank=True)
    post_Cat = models.ForeignKey(
        PostCategoryModel,
        related_name="blogs",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
