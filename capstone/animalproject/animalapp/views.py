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
        print('Error. There is no such profile.')

    return render(request, 'animalapp/animal_profile.html', context_dict)


def add_animal(request):
    """Rendering the page on which users add animals and submit the form."""

    if request.method == "POST":
        form = AnimalForm(request.POST)
        dog_form = DogForm(request.POST)
        cat_form = CatForm(request.POST)

        # if the user selects 'dog', only form and dog_form will be validated and saved
        if request.POST['species'] == 'dog' and form.is_valid() and dog_form.is_valid():
            form_instance = form.save()
            dog_form_instance = dog_form.save(commit=False)
            dog_form_instance.id = form_instance
            dog_form_instance.save()
            return HttpResponseRedirect('/animal_profile/{}/'.format(request.POST['id_number']))

        #if the user selects 'cat', only form and cat_form will be validated
        elif request.POST['species'] == 'cat' and form.is_valid() and cat_form.is_valid():
            form_instance = form.save()
            cat_form_instance = cat_form.save(commit=False)
            cat_form_instance.id = form_instance
            cat_form_instance.save()
            return HttpResponseRedirect('/animal_profile/{}/'.format(request.POST['id_number']))

        else:
            print(form.errors)
            print(dog_form.errors)
            print(cat_form.errors)
    else:
        form = AnimalForm()
        dog_form = DogForm()
        cat_form = CatForm()

    return render(request, 'animalapp/add_animal.html', {'form': form, 'dog_form': dog_form, 'cat_form': cat_form})

