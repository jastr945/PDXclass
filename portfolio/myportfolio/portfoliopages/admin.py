from django.contrib import admin
from .models import Project, Skill, Bio, ProfilePic
from django.db import models
from django.forms import TextInput


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '200'})},
    }


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Bio)
admin.site.register(ProfilePic)
