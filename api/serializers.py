from rest_framework import serializers
from .models import *


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordModel
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = "__all__"