from rest_framework import serializers
from .models import *


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordModel
        fields = [
            "id",
            "word",
            "antonyms",
            "synonyms",
            "example",
            "created_at",
            "description",
        ]


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategoryModel
        fields = fields = ["id", "cat_title", "cat_order"]


class PostSerializer(serializers.ModelSerializer):
    post_Cat = PostCategorySerializer(source="postCat", read_only=True)

    class Meta:
        model = PostModel
        fields = fields = ["id", "title", "image", "full_desc", "post_Cat"]


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = ["id", "heading", "description"]


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderModel
        fields = ["id", "site_title", "logo"]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageModel
        fields = ["id", "page_title", "page_description"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = [
            "id",
            "blog_title",
            "blog_description",
            "blog_image",
            "blog_author",
            "created_at",
        ]
