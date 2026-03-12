from rest_framework import viewsets, status, permissions
from rest_framework.permissions import AllowAny
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
    permission_classes = [AllowAny]


class PostCategoryViewSet(DefaultModelViewSet):
    queryset = PostCategoryModel.objects.prefetch_related("posts").all()
    serializer_class = PostCategorySerializer
    permission_classes = [AllowAny]
    


class PostViewSet(DefaultModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    

class FooterViewSet(DefaultModelViewSet):
    queryset = FooterModel.objects.all()
    serializer_class = FooterSerializer
    permission_classes = [AllowAny]
    

class HeaderViewSet(DefaultModelViewSet):
    queryset = HeaderModel.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [AllowAny]


class PageViewSet(DefaultModelViewSet):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer
    permission_classes = [AllowAny]


class BlogViewSet(DefaultModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


class UserViewSet(DefaultModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
