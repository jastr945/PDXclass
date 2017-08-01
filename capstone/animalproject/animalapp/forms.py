from django.forms import ModelForm
from .models import Animal, Dog, Cat


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        exclude = ['id']


class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ['id']


class CatForm(ModelForm):
    class Meta:
        model = Cat
        exclude = ['id']
