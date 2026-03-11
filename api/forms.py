from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class WordForm(forms.ModelForm):
    class Meta:
        model = WordModel
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "image", "full_desc", "postCat"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "postCat": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["postCat"].queryset = PostCategoryModel.objects.all()


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


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = "__all__"
