from django.urls import path
from .views import *

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
    #Footer
    path("api/footer/", FooterView, name="footer_list"),
    path("api/footer/<int:id>", FooterDetail, name="footer_detail"),
    path("api/footer/delete/<int:id>/", FooterDetail, name="delete_footer"),
    path("api/footer/edit/<int:id>/", FooterDetail, name="update_footer"),
    
    # Template URL
    # Word CRUD URL
    path("apiword/", adminWordListApi, name="apiword"),
    path("apiword/delete/<int:id>/", adminWordDelApi, name="deleteword"),
    path("apiword/edit/<int:id>/", adminWordUpdateApi, name="updateword"),
    # Post CRUD URL
    path("apipost/", adminPostListApi, name="apipost"),
    path("apipost/delete/<int:id>/", adminPostDelApi, name="deletepost"),
    path("apipost/edit/<int:id>/", adminPostUpdateApi, name="updatepost"),
    # Footer CRUD URL
    path("apifooter/", adminFooterListApi, name="apifooter"),
    path("apifooter/delete/<int:id>/", adminFooterDelApi, name="deletefooter"),
    path("apifooter/edit/<int:id>/", adminFooterUpdateApi, name="updatefooter"),
] 
