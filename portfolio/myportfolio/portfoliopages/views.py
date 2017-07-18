from django.shortcuts import render
from .models import Project

def index(request):

    projects = Project.objects.all()

    context_dict = {
        'projects': projects
    }
    return render(request, 'portfoliopages/index.html', context_dict)