from django.contrib import admin
from .models import *
from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = UserAdmin.fieldsets + (
#         ('Admin Info', {'fields': ('is_admin',)}),
#     )

# Register your models here.
admin.site.register([WordModel, PostModel, FooterModel, HeaderModel, PostCategoryModel, PageModel, BlogModel])