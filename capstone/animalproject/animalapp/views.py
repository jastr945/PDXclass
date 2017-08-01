from django.shortcuts import render
from .models import Animal
from .forms import AnimalForm, DogForm, CatForm


def index(request):
    """Rendering the main(index) page with a search tab."""
    return render(request, 'animalapp/index.html', {})


def animal_profile(request, animal_id_slug):
    """Rendering a single animal profile page."""
    context_dict = {}

    try:
        animals = Animal.objects.get(slug=animal_id_slug)
        context_dict['animals'] = animals

    except Animal.DoesNotExist:
        pass

    return render(request, 'animalapp/animal_profile.html', context_dict)


def add_animal(request):
    """Rendering the page on which users add animals."""
    form = AnimalForm()
    dog_form = DogForm()
    cat_form = CatForm()
    context_dict = {
        'form': form,
        'dog_form': dog_form,
        'cat_form': cat_form
    }
    return render(request, 'animalapp/add_animal.html', context_dict)