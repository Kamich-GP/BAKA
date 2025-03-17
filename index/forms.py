from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Готовая форма с изменениями
class RegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Обычная форма
class Search(forms.Form):
    search_bar = forms.CharField(max_length=32)
