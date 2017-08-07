from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Animal
from .forms import AnimalForm, DogForm, CatForm, SignUpForm
from django.conf import settings
from django.contrib import messages


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
    """Rendering a single animal profile page."""
    context_dict = {}

    try:
        animals = Animal.objects.get(slug=animal_id_slug)
        context_dict['animals'] = animals

    except Animal.DoesNotExist:
        print('Error. There is no such profile.')

    return render(request, 'animalapp/animal_profile.html', context_dict)


def add_animal(request):
    """Rendering the page on which users add, edit and delete database entries."""

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    animals = Animal.objects.all()

    if request.POST.get("submitButton"):
        form = AnimalForm(request.POST)
        dog_form = DogForm(request.POST)
        cat_form = CatForm(request.POST)
        tags = [request.POST['species']]

        # if the user selects 'dog', only form and dog_form will be validated and saved
        if request.POST['species'] == 'dog' and form.is_valid() and dog_form.is_valid():
            form_instance = form.save()
            dog_form_instance = dog_form.save(commit=False)
            dog_form_instance.id = form_instance
            dog_form_instance.save()
            tags.append(dog_form.data['dog_breed'].lower())
            tags.append(dog_form.data['dog_color'].lower())
            form_instance.tags.add(*tags)
            return HttpResponseRedirect('/animal_profile/{}/'.format(request.POST['id_number']))

        # if the user selects 'cat', only form and cat_form will be validated and saved
        elif request.POST['species'] == 'cat' and form.is_valid() and cat_form.is_valid():
            form_instance = form.save()
            cat_form_instance = cat_form.save(commit=False)
            cat_form_instance.id = form_instance
            cat_form_instance.save()
            tags.append(cat_form.data['cat_breed'].lower())
            tags.append(cat_form.data['cat_color'].lower())
            form_instance.tags.add(*tags)
            return HttpResponseRedirect('/animal_profile/{}/'.format(request.POST['id_number']))

        else:
            messages.error(request, form.errors)

    elif request.POST.get("deleteButton"):
        get_object_or_404(Animal, name=request.POST['deleteButton']).delete()
        return HttpResponseRedirect('/add_animal/')

    else:
        form = AnimalForm()
        dog_form = DogForm()
        cat_form = CatForm()

    return render(request, 'animalapp/add_animal.html', {'form': form, 'dog_form': dog_form, 'cat_form': cat_form,
                                                         'animals': animals})


def search_results(request):
    """Rendering the search results page; the results are filtered by species or a user's search string."""

    if request.GET.get("searchField"):
        search_string_list = request.GET['searchField'].lower().split(' ')
        animals = Animal.objects.filter(tags__name__in=search_string_list)
    elif request.GET.get("allDogs"):
        animals = Animal.objects.filter(species='dog')
    else:
        animals = Animal.objects.filter(species='cat')

    return render(request, 'animalapp/search_results.html', {'animals': animals})
