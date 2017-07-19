from django.shortcuts import render
from .models import Project, Skill

def index(request):

    projects = Project.objects.all()
    skills = Skill.objects.all()

    context_dict = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfoliopages/index.html', context_dict)