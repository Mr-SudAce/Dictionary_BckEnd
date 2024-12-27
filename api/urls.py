from django.urls import path
from .views import *

urlpatterns = [
    # API URL
    
    ########################## Word #######################
    path("api/word/post/", CreateWord, name="create_post_word"),
    path("api/word/all/", GetAllWord, name="get_word"),
    path("api/word/<int:id>/", GetWordById, name="get_wordby_id"),
    path("api/word/update/<int:id>/", UpdateWord, name="update_word"),
    path("api/word/delete/<int:id>/", DeleteWord, name="delete_word"),
    ########################## Word #######################
    
    ####################### POST CATEGORY #######################
    path("api/postcat/post/", CreatePostCategory, name="create_postcat"),
    path("api/postcat/all/", GetAllCategories, name="postcat_list"),
    path("api/postcat/<int:id>/", GetCategoriesById, name="get_postcatby_id"),
    path("api/postcat/update/<int:id>/", UpdateCategory, name="update_postcat"),
    path("api/postcat/delete/<int:id>/", DeleteCategory, name="delete_postcat"),
    ####################### POST CATEGORY #######################
    
    ####################### POST #######################
    path("api/post/post/", CreatePost, name="create_post"),
    path("api/post/all/", GetAllPost, name="post_list"),
    path("api/post/<int:id>/", GetAllPostById, name="get_postby_id"),
    path("api/post/update/<int:id>/", UpdatePost, name="update_post"),
    path("api/post/delete/<int:id>/", DeletePost, name="delete_post"),
    ####################### POST #######################
    ####################### Footer #######################
    path("api/footer/post/", CreateFooter, name="create_footer"),
    path("api/footer/all/", GetAllFooter, name="footer_list"),
    path("api/footer/<int:id>/", GetAllFooterById, name="get_footerby_id"),
    path("api/footer/delete/<int:id>/", DeleteFooter, name="delete_footer"),
    path("api/footer/update/<int:id>/", UpdateFooter, name="update_footer"),
    ####################### Footer #######################
    ####################### Header #######################
    path("api/header/post/", CreateHeader, name="create_header"),
    path("api/header/all/", GetAllHeader, name="header_list"),
    path("api/header/<int:id>/", GetAllHeaderById, name="get_headerby_id"),
    path("api/header/delete/<int:id>/", DeleteHeader, name="delete_header"),
    path("api/header/update/<int:id>/", UpdateHeader, name="update_header"),
    ####################### Header #######################






    ########################## Template URL #######################
    # Word CRUD URL
    path("apiword/", adminWordListApi, name="apiword"),
    path("apiword/delete/<int:id>/", adminWordDelApi, name="deleteword"),
    path("apiword/edit/<int:id>/", adminWordUpdateApi, name="updateword"),
    # Post CRUD URL
    path("apipost/", adminPostListApi, name="apipost"),
    path("apipost/delete/<int:id>/", adminPostDelApi, name="deletepost"),
    path("apipost/edit/<int:id>/", adminPostUpdateApi, name="updatepost"),
    # Post CATEGORY CRUD URL
    path("apipostcat/", adminPostCateListApi, name="apipostcat"),
    path("apipostcat/delete/<int:id>/", adminPostCateDelApi, name="deletepostcat"),
    path("apipostcat/edit/<int:id>/", adminPostCateUpdateApi, name="updatepostcat"),
    # Footer CRUD URL
    path("apifooter/", adminFooterListApi, name="apifooter"),
    path("apifooter/delete/<int:id>/", adminFooterDelApi, name="deletefooter"),
    path("apifooter/edit/<int:id>/", adminFooterUpdateApi, name="updatefooter"),
    # Header CRUD URL
    path("apiheader/", adminHeaderListApi, name="apiheader"),
    path("apiheader/delete/<int:id>/", adminHeaderDelApi, name="deleteheader"),
    path("apiheader/edit/<int:id>/", adminHeaderUpdateApi, name="updateheader"),

]
