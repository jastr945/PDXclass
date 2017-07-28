from django.db import models

def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)


class Animal(models.Model):
    """
    Animal profile structure.
    """
    name = models.CharField(max_length=50)
    id_number = models.IntegerField()

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='')
    breed = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

    SURGERY_CHOICES = (
        ('yes', 'yes'),
        ('no', 'no')
    )

    surgery = models.CharField(max_length=20, choices=SURGERY_CHOICES, default='')
    location = models.CharField(max_length=50)
    intake_date = models.DateField()

    STATUS_CHOICES = (
        ('av', 'available'),
        ('temp', 'temporarily unavailable'),
        ('oh', 'on hold'),
        ('adt', 'ADOPTED')
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='av')
    personality = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return '{}'.format(self.name)


