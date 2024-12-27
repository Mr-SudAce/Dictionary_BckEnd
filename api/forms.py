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

class FooterForm(forms.ModelForm):
    class Meta:
        model = FooterModel
        fields = "__all__"

class HeaderForm(forms.ModelForm):
    class Meta:
        model = HeaderModel
        fields = "__all__"

class PostCatForm(forms.ModelForm):
    class Meta:
        model = PostCategoryModel
        fields = "__all__"

class PageForm(forms.ModelForm):
    class Meta:
        model = PageModel
        fields = "__all__"