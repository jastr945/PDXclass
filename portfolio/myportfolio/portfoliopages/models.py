from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image


def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    img = models.ImageField(upload_to=profile_upload_handler)
    description = models.CharField(max_length=100)
    project_link = models.CharField(max_length=500, blank=True, null=True)
    readme_link = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         super().save(*args, **kwargs)
    #         path = self.img.path
    #         image = Image.open(path)
    #         width = self.img.width * .5
    #         img = image.resize((int(width), int(width)))
    #         img.save(path)
    #     else:
    #         super().save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Bio(models.Model):
    name = 'Bio'
    text = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Bio'


class ProfilePic(models.Model):
    name = 'Profile picture'
    img = models.ImageField(upload_to=profile_upload_handler)

    def __str__(self):
        return '{}'.format(self.name)