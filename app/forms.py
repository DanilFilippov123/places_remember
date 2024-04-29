from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from app.models import Place


class PlaceForm(forms.ModelForm):
    name = forms.CharField(label='Название места')
    comment = forms.CharField(label='Комментарий')
    lat = forms.FloatField(widget=forms.HiddenInput())
    lng = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Place
        fields = ['name', 'comment', 'lat', 'lng']


class RegisterUserForm(UserCreationForm):
    photo = forms.ImageField(label='Фото профиля', required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'photo']
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }
