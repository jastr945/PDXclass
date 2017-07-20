from django.contrib import admin
from .models import Project, Skill, Bio, ProfilePic

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Bio)
admin.site.register(ProfilePic)