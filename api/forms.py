from .models import *
from django import forms


class WordForm(forms.ModelForm):
    class Meta:
        model = WordModel
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"