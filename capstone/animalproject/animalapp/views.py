from django.shortcuts import render
from .models import Animal

# rendering the main page with the search tab
def index(request):
    return render(request, 'animalapp/index.html', {})

# rendering a single animal profile page
def animal_profile(request):
    animals = Animal.objects.all()
    context_dict = {'animals': animals}
    return render(request, 'animalapp/animal_profile.html', context_dict)
