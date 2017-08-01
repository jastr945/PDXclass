from django.forms import ModelForm
from .models import Animal, Dog, Cat
from django import forms

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        exclude = ['id']
        birthday = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))

class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ['id']


class CatForm(ModelForm):
    class Meta:
        model = Cat
        exclude = ['id']
