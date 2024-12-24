from rest_framework import serializers
from .models import *


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordModel
        fields = "__all__"
        

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategoryModel
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    postCat = serializers.PrimaryKeyRelatedField(
        many=True, queryset=PostCategoryModel.objects.all()
    )
    class Meta:
        model = PostModel
        fields = "__all__"
        

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = "__all__"

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderModel
        fields = "__all__"

