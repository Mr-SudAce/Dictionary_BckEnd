from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([WordModel, PostModel, FooterModel, HeaderModel, PostCategoryModel, PageModel, BlogModel])