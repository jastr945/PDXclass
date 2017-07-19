from django.db import models
from PIL import Image


def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)


class Project(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to=profile_upload_handler)
    description = models.CharField(max_length=100)
    project_link = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.name)

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