from django.forms import ModelForm, TextInput, EmailInput
from .models import Client, Seller


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['password', 'email', 'first_name', 'username', 'is_active']
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Name",
            }),
            "username": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Nickname",
            }),
            "email": EmailInput(attrs={
                'class': 'form__input',
                'placeholder': "Email address",
            }),
            "password": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Password",
            })
        }


class NewSellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['password', 'email', 'first_name', 'username',
                  'country', 'is_active']
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Name",
            }),
            "username": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Nickname",
            }),
            "country": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Country",
            }),
            "email": EmailInput(attrs={
                'class': 'form__input',
                'placeholder': "Email address",
            }),
            "password": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Password",
            })
        }


class AuthenticationForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['password', 'username']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Nickname",
            }),
            "password": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Password",
            })
        }
