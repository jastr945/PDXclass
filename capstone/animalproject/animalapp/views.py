from django.shortcuts import render, HttpResponseRedirect
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
    """Rendering the page on which users add animals and submit the form."""

    if request.method == "POST":
        form = AnimalForm(request.POST)
        dog_form = DogForm(request.POST)
        cat_form = CatForm(request.POST)

        if form.is_valid() and dog_form.is_valid() and cat_form.is_valid():

            form_instance = form.save(commit=False)
            dog_form_instance = dog_form.save(commit=False)
            cat_form_instance = cat_form.save(commit=False)

            form_instance.save()
            dog_form_instance.save()
            cat_form_instance.save()
            return HttpResponseRedirect('/')
    else:
        form = AnimalForm()
        dog_form = DogForm()
        cat_form = CatForm()

    return render(request, 'animalapp/add_animal.html', {'form': form, 'dog_form': dog_form, 'cat_form': cat_form})

