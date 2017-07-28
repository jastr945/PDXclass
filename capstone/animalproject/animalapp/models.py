from django.db import models
import datetime

def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)


class Animal(models.Model):
    """
    Animal profile structure.
    """
    name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='')

    BREED_CHOICES = (
        ('Domestic shorthair/mix', 'Domestic shorthair/mix'),
        ('Persian', 'Persian'),
        ('Siamese', 'Siamese')
    )
    breed = models.CharField(max_length=50, choices=BREED_CHOICES, default='Domestic shorthair/mix')
    birthday = models.DateField(blank=True, null=True)

    SURGERY_CHOICES = (
        ('yes', 'yes'),
        ('no', 'no')
    )

    surgery = models.CharField(max_length=20, choices=SURGERY_CHOICES, default='', verbose_name='Spayed/neutered')

    VACCINE_CHOICES = (
        ('yes', 'yes'),
        ('no', 'no')
    )

    vaccine = models.CharField(max_length=20, choices=VACCINE_CHOICES, default='yes', verbose_name='Vaccinated')

    LOCATION_CHOICES = (
        ('OFOSA shelter', 'OFOSA shelter'),
        ('PetSmart Tanasbourne', 'PetSmart Tanasbourne'),
        ('PetSmart Wilsonville', 'PetSmart Wilsonville'),
        ('PetSmart Cedar Hills', 'PetSmart Cedar Hills'),
        ('PetSmart Hillsboro', 'PetSmart Hillsboro'),
        ('Foster home', 'Foster home')
    )

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='')

    intake_date = models.DateField(blank=True, null=True)

    STATUS_CHOICES = (
        ('available', 'available'),
        ('temporarily unavailable', 'temporarily unavailable'),
        ('on hold', 'on hold'),
        ('ADOPTED', 'ADOPTED')
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    personality = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return '{}'.format(self.name)

    def age(self):
        dob = self.birthday
        tod = datetime.date.today()
        dob_days = int(dob.year) * 365 + int(dob.month) * 30 + int(dob.day)
        tod_days = int(tod.year) * 365 + int(tod.month) * 30 + int(tod.day)
        age_days = tod_days - dob_days
        animal_year = age_days // 365
        animal_month = (age_days - animal_year * 365) // 30
        animal_day = age_days - animal_year * 365 - animal_month * 30
        return '{}y {}m {}d'.format(animal_year, animal_month, animal_day)

    animal_age = property(age)

