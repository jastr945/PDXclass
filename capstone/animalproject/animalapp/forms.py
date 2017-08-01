from django.forms import ModelForm
from .models import Animal, Dog


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        exclude = ['id']


class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ['id']