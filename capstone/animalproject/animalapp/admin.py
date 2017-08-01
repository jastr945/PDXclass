from django.contrib import admin
from django.db import models
from .models import Animal, Cat, Dog
from django.forms import TextInput


class AnimalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('id_number',)}
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '200'})},
    }

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Cat)
admin.site.register(Dog)