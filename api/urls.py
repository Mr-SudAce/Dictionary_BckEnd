from django.urls import path
from .views import *

urlpatterns = [
    
    path("", supermain, name="supermain"),

    
    #  admin Login/ register
    path('register/', auth_register, name='auth_register'),
    path('login/', auth_login, name='auth_login'),
    path('logout/', auth_logout, name='auth_logout'),
    
    
    
    # API URL
    
    ########################## User #######################
    path("api/user/", CreateUser, name="create_post_user"),
    path("api/all/user/", GetAllUser, name="get_alluser"),
    path("api/user/<int:id>/", GetUserById, name="get_userby_id"),
    path("api/user/update/<int:id>/", UpdateUser, name="update_user"),
    path("api/user/delete/<int:id>/", DeleteUser, name="delete_user"),
    ########################## User #######################
    
    
    
    
    ########################## Word #######################
    path("api/word/", CreateWord, name="create_post_word"),
    path("api/all/word/", GetAllWord, name="get_allword"),
    path("api/word/<int:id>/", GetWordById, name="get_wordby_id"),
    path("api/word/update/<int:id>/", UpdateWord, name="update_word"),
    path("api/word/delete/<int:id>/", DeleteWord, name="delete_word"),
    ########################## Word #######################
    ####################### POST CATEGORY #######################
    path("api/postcat/", CreatePostCategory, name="create_postcat"),
    path("api/all/postcat/", GetAllCategories, name="get_allpostcat"),
    path("api/postcat/<int:id>/", GetCategoriesById, name="get_postcatby_id"),
    path("api/postcat/update/<int:id>/", UpdateCategory, name="update_postcat"),
    path("api/postcat/delete/<int:id>/", DeleteCategory, name="delete_postcat"),
    ####################### POST CATEGORY #######################
    ####################### POST #######################
    path("api/post/", CreatePost, name="create_post"),
    path("api/all/post/", GetAllPost, name="get_allpost"),
    path("api/post/<int:id>/", GetAllPostById, name="get_postby_id"),
    path("api/post/update/<int:id>/", UpdatePost, name="update_post"),
    path("api/post/delete/<int:id>/", DeletePost, name="delete_post"),
    ####################### POST #######################
    ####################### Footer #######################
    path("api/footer/", CreateFooter, name="create_footer"),
    path("api/all/footer/", GetAllFooter, name="get_allfooter"),
    path("api/footer/<int:id>/", GetAllFooterById, name="get_footerby_id"),
    path("api/footer/delete/<int:id>/", DeleteFooter, name="delete_footer"),
    path("api/footer/update/<int:id>/", UpdateFooter, name="update_footer"),
    ####################### Footer #######################
    ####################### Header #######################
    path("api/header/", CreateHeader, name="create_header"),
    path("api/all/header/", GetAllHeader, name="get_allheader"),
    path("api/header/<int:id>/", GetAllHeaderById, name="get_headerby_id"),
    path("api/header/delete/<int:id>/", DeleteHeader, name="delete_header"),
    path("api/header/update/<int:id>/", UpdateHeader, name="update_header"),
    ####################### Header #######################
    ####################### Page #######################
    path("api/page/", CreatePage, name="create_page"),
    path("api/all/page/", GetAllPage, name="get_allpage"),
    path("api/page/<int:id>/", GetAllPageById, name="get_pageby_id"),
    path("api/page/delete/<int:id>/", DeletePage, name="delete_page"),
    path("api/page/update/<int:id>/", UpdatePage, name="update_page"),
    ####################### Page #######################
    ####################### Blog #######################
    path("api/blog/", CreateBlog, name="create_blog"),
    path("api/all/blog/", GetAllBlog, name="get_allblog"),
    path("api/blog/<int:id>/", GetAllBlogById, name="get_blogby_id"),
    path("api/blog/delete/<int:id>/", DeleteBlog, name="delete_blog"),
    path("api/blog/update/<int:id>/", UpdateBlog, name="update_blog"),
    ####################### Blog #######################
    
    
    ########################## Template URL #######################
    
    
    # USER CRUD URL
    path("user/", userListApi, name='apiuser'),
    path("user/delete/<int:id>/", userDelApi, name='deleteuser'),
    path("user/edit/<int:id>/", userUpdateApi, name='updateuser'),
    # Word CRUD URL
    path("word/", adminWordListApi, name="apiword"),
    path("word/delete/<int:id>/", adminWordDelApi, name="deleteword"),
    path("word/edit/<int:id>/", adminWordUpdateApi, name="updateword"),
    # Post CRUD URL
    path("post/", adminPostListApi, name="apipost"),
    path("post/delete/<int:id>/", adminPostDelApi, name="deletepost"),
    path("post/edit/<int:id>/", adminPostUpdateApi, name="updatepost"),
    # Post CATEGORY CRUD URL
    path("postcat/", adminPostCateListApi, name="apipostcat"),
    path("postcat/delete/<int:id>/", adminPostCateDelApi, name="deletepostcat"),
    path("postcat/edit/<int:id>/", adminPostCateUpdateApi, name="updatepostcat"),
    # Footer CRUD URL
    path("footer/", adminFooterListApi, name="apifooter"),
    path("footer/delete/<int:id>/", adminFooterDelApi, name="deletefooter"),
    path("footer/edit/<int:id>/", adminFooterUpdateApi, name="updatefooter"),
    # Header CRUD URL
    path("header/", adminHeaderListApi, name="apiheader"),
    path("header/delete/<int:id>/", adminHeaderDelApi, name="deleteheader"),
    path("header/edit/<int:id>/", adminHeaderUpdateApi, name="updateheader"),
    # Page CRUD URL
    path("page/", adminPageListApi, name="apipage"),
    path("page/delete/<int:id>/", adminPageDelApi, name="deletepage"),
    path("page/edit/<int:id>/", adminPageUpdateApi, name="updatepage"),
    # Blog CRUD URL
    path("blog/", adminBlogListApi, name="apiblog"),
    path("blog/delete/<int:id>/", adminBlogDelApi, name="deleteblog"),
    path("blog/edit/<int:id>/", adminBlogUpdateApi, name="updateblog"),
]