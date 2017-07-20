from django.shortcuts import render
from .models import Project, Skill, Bio, ProfilePic

def index(request):

    projects = Project.objects.all()
    skills = Skill.objects.all()
    bio = Bio.objects.all()
    profile_pic = ProfilePic.objects.all()

    context_dict = {
        'projects': projects,
        'skills': skills,
        'bio': bio,
        'profile_pic': profile_pic,
    }
    return render(request, 'portfoliopages/index.html', context_dict)