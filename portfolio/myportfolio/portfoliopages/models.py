from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image


def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    img = models.ImageField(upload_to=profile_upload_handler)
    description = models.TextField(max_length=255)
    demo_link = models.CharField(max_length=500, blank=True, null=True)
    project_link = models.CharField(max_length=500, blank=True, null=True)
    readme_link = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Bio(models.Model):
    name = 'Bio'
    text = models.TextField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Bio'


class ProfilePic(models.Model):
    name = 'Profile picture'
    img = models.ImageField(upload_to=profile_upload_handler)

    def __str__(self):
        return '{}'.format(self.name)
