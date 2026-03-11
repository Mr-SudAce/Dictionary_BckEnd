from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .api_views import (
    WordViewSet,
    PostCategoryViewSet,
    PostViewSet,
    FooterViewSet,
    HeaderViewSet,
    PageViewSet,
    BlogViewSet,
    UserViewSet,
)

# REST API router
router = DefaultRouter()
router.register(r'all/word', WordViewSet, basename='word')
router.register(r'all/postcat', PostCategoryViewSet, basename='postcategory')
router.register(r'all/post', PostViewSet, basename='post')
router.register(r'all/footer', FooterViewSet, basename='footer')
router.register(r'all/header', HeaderViewSet, basename='header')
router.register(r'all/page', PageViewSet, basename='page')
router.register(r'all/blog', BlogViewSet, basename='blog')
router.register(r'all/user', UserViewSet, basename='user')


urlpatterns = [
    # DRF-generated endpoints (list/create/retrieve/update/delete)
    path('api/', include(router.urls)),

    path("", supermain, name="supermain"),

    
    #  admin Login/ register
    path('register/', auth_register, name='auth_register'),
    path('login/', auth_login, name='auth_login'),
    path('logout/', auth_logout, name='auth_logout'),
    
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