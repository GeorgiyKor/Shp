from django import forms
from shp.models import Item

from django.contrib.auth.models import User

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddItemForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class LoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='first', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'image')
