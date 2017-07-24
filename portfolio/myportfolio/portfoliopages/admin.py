from django.contrib import admin
from .models import Project, Skill, Bio, ProfilePic

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Bio)
admin.site.register(ProfilePic)
