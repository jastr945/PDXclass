from django.shortcuts import render
from .models import Project, Skill, Bio, ProfilePic


# rendering the main page
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


#rendering a project page
def project(request, project_name_slug):

    context_dict = {}

    try:
        myproject = Project.objects.get(slug=project_name_slug)
        context_dict['myproject'] = myproject
    except Project.DoesNotExist:
        context_dict['myproject'] = None
    return render(request, 'portfoliopages/{}.html'.format(project_name_slug), context_dict)
