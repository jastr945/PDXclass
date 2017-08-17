from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Animal, Image
from .forms import AnimalForm, DogForm, CatForm, SignUpForm
from .filters import AnimalFilter
from django.conf import settings
from django.contrib import messages
import datetime
import re


def signup(request):
    """Rendering the sign-up page."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('add_animal')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    """Rendering the login page."""
    return login(request)


def logout_view(request):
    """Logs a user out and redirects to the main(index) page."""
    logout(request)


def index(request):
    """Rendering the main(index) page with a search tab."""
    return render(request, 'animalapp/index.html', {})


def animal_profile(request, animal_id_slug):
    """Rendering a single animal profile page.
    Clicking a tag field results in redirecting to the search results page filtered by a tag name.
    """
    context_dict = {}

    if request.GET.get('tag'):
        return HttpResponseRedirect('/search_results/?search={}'.format(request.GET['tag']))
    try:
        animals = Animal.objects.get(slug=animal_id_slug)
        context_dict['animals'] = animals

    except Animal.DoesNotExist:
        print('Error. There is no such profile.')

    return render(request, 'animalapp/animal_profile.html', context_dict)


def add_animal(request):
    """Rendering the page on which users add, edit and delete database entries."""

    # redirecting to add_animal page after logging in
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    animals = Animal.objects.all()

    # splits fields containing several words into a list of separate words
    def clear_tags(raw_data: str):
        cleaned = (re.sub('[\/\-]+', ' ', raw_data)).split(' ')
        return cleaned

    if request.POST.get("submitButton"):
        form = AnimalForm(request.POST)
        dog_form = DogForm(request.POST)
        cat_form = CatForm(request.POST)
        tags = [request.POST['species'], request.POST['name'].lower()]

        # creating 'male' or 'female' tags
        if request.POST['gender'] == 'True':
            tags.append('male')
        else:
            tags.append('female')

        # calculating animal's age in days in order to add an appropriate tag (kitten/puppy/adult)
        tod = datetime.date.today()
        dob = int(dog_form.data['birthday_year']) * 365 + int(dog_form.data['birthday_month']) * 30 + int(dog_form.data['birthday_day'])
        age = (int(tod.year) * 365 + int(tod.month) * 30 + int(tod.day)) - dob

        # if the user selects 'dog', only form and dog_form will be validated and saved
        if request.POST['species'] == 'dog' and form.is_valid() and dog_form.is_valid():
            form_instance = form.save()
            dog_form_instance = dog_form.save(commit=False)
            dog_form_instance.id = form_instance
            dog_form_instance.save()

            # rendering multiple images for each dog profile
            for img in request.FILES.getlist('img'):
                Image.objects.create(img=img, pet=Animal.objects.get(pk=dog_form_instance.id.pk))

            # parses a breed name, if it consists of more than one word, and renders one-word tags
            if len(clear_tags(dog_form.data['dog_breed'])) > 1:
                i = 0
                list_length = len(clear_tags(dog_form.data['dog_breed']))
                while i < list_length:
                    tags.append(clear_tags(dog_form.data['dog_breed'])[i].lower())
                    i += 1
            else:
                tags.append(dog_form.data['dog_breed'].lower())

            if age < 365:
                tags.append('puppy')
            else:
                tags.append('adult')

            tags.append(dog_form.data['dog_color'])
            tags.append(dog_form.data['size'])
            form_instance.tags.add(*tags)
            return HttpResponseRedirect('/animal_profile/{}/'.format(request.POST['id_number']))

        # if the user selects 'cat', only form and cat_form will be validated and saved
        elif request.POST['species'] == 'cat' and form.is_valid() and cat_form.is_valid():
            form_instance = form.save()
            cat_form_instance = cat_form.save(commit=False)
            cat_form_instance.id = form_instance
            cat_form_instance.save()

            # rendering multiple images for each cat profile
            for img in request.FILES.getlist('img'):
                Image.objects.create(img=img, pet=Animal.objects.get(pk=cat_form_instance.id.pk))

            # parses a breed name, if it consists of more than one word, and renders one-word tags
            if len(clear_tags(cat_form.data['cat_breed'])) > 1:
                i = 0
                list_length = len(clear_tags(cat_form.data['cat_breed']))
                while i < list_length:
                    tags.append(clear_tags(cat_form.data['cat_breed'])[i].lower())
                    i += 1
            else:
                tags.append(cat_form.data['cat_breed'].lower())

            # parses a color name, if it consists of more than one word, and renders one-word tags
            if len(clear_tags(cat_form.data['cat_color'])) > 1:
                i = 0
                list_length = len(clear_tags(cat_form.data['cat_color']))
                while i < list_length:
                    tags.append(clear_tags(cat_form.data['cat_color'])[i].lower())
                    i += 1
            else:
                tags.append(cat_form.data['cat_color'].lower())

            if age < 365:
                tags.append('kitten')
            else:
                tags.append('adult')

            form_instance.tags.add(*tags)
            return HttpResponseRedirect('/animal_profile/{}/'.format(request.POST['id_number']))

        else:
            messages.error(request, form.errors)

    # deleting a profile
    elif request.POST.get("deleteButton"):
        get_object_or_404(Animal, id=request.POST['animalID']).delete()
        return HttpResponseRedirect('/add_animal/')

    else:
        form = AnimalForm()
        dog_form = DogForm()
        cat_form = CatForm()

    return render(request, 'animalapp/add_animal.html', {'form': form, 'dog_form': dog_form, 'cat_form': cat_form,
                                                         'animals': animals})


def search_results(request):
    """Rendering the search results page; the results are filtered by species or a user's search string.
       If the string is empty, the search will return all available entries.
       Once the page is rendered, search results can be filtered by gender and location.
    """

    if request.GET.get("search"):
        search_string_list = request.GET['search'].lower().split(' ')
        animals = Animal.objects.filter(tags__name__in=search_string_list)
        filtered_animals = AnimalFilter(request.GET, queryset=animals)
    elif request.GET.get("allDogs"):
        dogs = Animal.objects.filter(species='dog')
        filtered_animals = AnimalFilter(request.GET, queryset=dogs)
    elif request.GET.get("allCats"):
        cats = Animal.objects.filter(species='cat')
        filtered_animals = AnimalFilter(request.GET, queryset=cats)
    else:
        # from ipdb import set_trace;set_trace()
        animals = Animal.objects.all()
        filtered_animals = AnimalFilter(request.GET, queryset=animals)

    return render(request, 'animalapp/search_results.html', {'filtered_animals': filtered_animals})

