from django.shortcuts import render
from .models import Animal

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
