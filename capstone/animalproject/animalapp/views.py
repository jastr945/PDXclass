from django.shortcuts import render
from .models import Animal
from .forms import AnimalForm, DogForm

# rendering the main page with the search tab
def index(request):
    return render(request, 'animalapp/index.html', {})

# rendering a single animal profile page
def animal_profile(request, animal_id_slug):
    context_dict = {}

    try:
        animals = Animal.objects.get(slug=animal_id_slug)
        context_dict['animals'] = animals

    except Animal.DoesNotExist:
        pass

    return render(request, 'animalapp/animal_profile.html', context_dict)


def add_animal(request):

    form = AnimalForm()
    dog_form = DogForm()
    context_dict = {
        'form': form,
        'dog_form': dog_form
    }
    return render(request, 'animalapp/add_animal.html', context_dict)