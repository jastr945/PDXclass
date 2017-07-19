from django.shortcuts import render
from .models import Project, Skill, Bio

def index(request):

    projects = Project.objects.all()
    skills = Skill.objects.all()
    bio = Bio.objects.all()

    context_dict = {
        'projects': projects,
        'skills': skills,
        'bio': bio,
    }
    return render(request, 'portfoliopages/index.html', context_dict)