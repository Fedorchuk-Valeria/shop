from django.forms import ModelForm, TextInput, FileInput, NumberInput, URLInput
from .models import Product


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'number', 'pic', 'price', 'rating', 'product_type', 'seller']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Name",
            }),
            "number": NumberInput(attrs={
                'class': 'form__input',
                'placeholder': "Number",
            }),
            "pic": URLInput(attrs={
                'placeholder': "Image",
            }),
            "price": NumberInput(attrs={
                'class': 'form__input',
                'placeholder': "Price",
            }),
            "product_type": TextInput(attrs={
                'class': 'form__input',
                'placeholder': "Type",
            })
        }
