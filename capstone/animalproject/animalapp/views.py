from django.shortcuts import render

# rendering the main page with the search tab
def index(request):
    return render(request, 'animalapp/index.html', {})
