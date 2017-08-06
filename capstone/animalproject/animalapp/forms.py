from django.forms import ModelForm
from .models import Animal, Dog, Cat
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import TextInput
import datetime


class AnimalForm(ModelForm):

    intake_date = forms.DateField(initial=datetime.date.today(), widget=SelectDateWidget(years=(range(datetime.date.today().year - 10, datetime.date.today().year + 1))))

    GENDER_CHOICES = [('0', 'male'), ('1', 'female')]

    CHOICES = [('0', 'yes'), ('1', 'no')]

    gender = forms.TypedChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    surgery = forms.TypedChoiceField(choices=CHOICES, initial='0', widget=forms.RadioSelect)

    vaccine = forms.TypedChoiceField(choices=CHOICES, initial='0', widget=forms.RadioSelect)

    class Meta:
        model = Animal
        exclude = ['id', 'slug']
        widgets = {
            'birthday': SelectDateWidget(years=(range(datetime.date.today().year - 20, datetime.date.today().year + 1))),
            'notes': TextInput(attrs={'placeholder': 'Describe any special needs, etc.'})
        }



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
