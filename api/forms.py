from .models import Word
from django import forms


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'