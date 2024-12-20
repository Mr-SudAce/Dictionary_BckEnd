from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # API URL
    # Word
    path("api/word/", WordView, name="word_list"),
    path("api/word/<int:id>", WordDetail, name="word_detail"),
    path("api/word/delete/<int:id>/", WordDetail, name="delete_word"),
    path("api/word/edit/<int:id>/", WordDetail, name="update_word"),
    
    # POST
    path("api/post/", PostView, name="post_list"),
    path("api/post/<int:id>", PostDetail, name="post_detail"),
    path("api/post/delete/<int:id>/", PostDetail, name="delete_post"),
    path("api/post/edit/<int:id>/", PostDetail, name="update_post"),
    
    
    
    
    
    
    # Template URL
    # Word CRUD URL
    path("apiword/", adminWordListApi, name="apiword"),
    path("apiword/delete/<int:id>/", adminWordDelApi, name="deleteword"),
    path("apiword/edit/<int:id>/", adminWordUpdateApi, name="updateword"),
    
    
    
    
    # Post CRUD URL
    path("apipost/", adminPostListApi, name="apipost"),
    path("apipost/delete/<int:id>/", adminPostDelApi, name="deletepost"),
    path("apipost/edit/<int:id>/", adminPostUpdateApi, name="updatepost"),
    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
