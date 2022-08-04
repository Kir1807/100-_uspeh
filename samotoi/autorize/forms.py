from .models import users
from django.forms import ModelForm, TextInput


class usersForm(ModelForm):
    class Meta:
        model = users
        fields = ['name', 'password']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'iliatortuga@gmail.com'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введите пароль'
            }),
        }