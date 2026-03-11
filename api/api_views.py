from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import (
    WordModel,
    PostCategoryModel,
    PostModel,
    FooterModel,
    HeaderModel,
    PageModel,
    BlogModel,
)
from .serializers import (
    WordSerializer,
    PostCategorySerializer,
    PostSerializer,
    FooterSerializer,
    HeaderSerializer,
    PageSerializer,
    BlogSerializer,
    UserSerializer,
)


class DefaultModelViewSet(viewsets.ModelViewSet):
    """Base viewset that ensures only admins can access the API."""
    permission_classes = [permissions.IsAdminUser]


class WordViewSet(DefaultModelViewSet):
    queryset = WordModel.objects.all()
    serializer_class = WordSerializer


class PostCategoryViewSet(DefaultModelViewSet):
    queryset = PostCategoryModel.objects.prefetch_related("posts").all()
    serializer_class = PostCategorySerializer


class PostViewSet(DefaultModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class FooterViewSet(DefaultModelViewSet):
    queryset = FooterModel.objects.all()
    serializer_class = FooterSerializer


class HeaderViewSet(DefaultModelViewSet):
    queryset = HeaderModel.objects.all()
    serializer_class = HeaderSerializer


class PageViewSet(DefaultModelViewSet):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer


class BlogViewSet(DefaultModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class UserViewSet(DefaultModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
