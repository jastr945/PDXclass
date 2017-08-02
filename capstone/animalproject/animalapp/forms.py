from django.forms import ModelForm
from .models import Animal, Dog, Cat
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        exclude = ['id', 'slug']
        birthday = forms.DateField()


class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ['id']


class CatForm(ModelForm):
    class Meta:
        model = Cat
        exclude = ['id']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text=None)
    last_name = forms.CharField(max_length=30, help_text=None)
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')
    password1 = forms.CharField(max_length=254, help_text='Your password must contain at least 8 characters, and they can\'t be all numeric.')
    password2 = forms.CharField(max_length=254, help_text=None)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
