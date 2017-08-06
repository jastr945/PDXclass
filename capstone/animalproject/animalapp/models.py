from django.db import models
import datetime
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator


def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)


class Animal(models.Model):
    """
    An abstract class containing basic information about each animal.
    """

    SPECIES_CHOICES = (
        ('dog', 'dog'),
        ('cat', 'cat')
    )

    species = models.CharField(max_length=50, choices=SPECIES_CHOICES, default='', blank=True)

    name = models.CharField(max_length=50, default='', unique=True)

    id_number = models.CharField(max_length=50, default='', unique=True)

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='', blank=True)
    birthday = models.DateField(blank=True, null=False)

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

    intake_date = models.DateField(blank=False, null=False)

    STATUS_CHOICES = (
        ('available', 'available'),
        ('temporarily unavailable', 'temporarily unavailable'),
        ('on hold', 'on hold'),
        ('ADOPTED', 'ADOPTED')
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    HOME_CHOICES = (
        ('young children', 'young children'),
        ('cats', 'cats'),
        ('dogs', 'dogs')
    )

    home = models.CharField(max_length=255, blank=True, default='', choices=HOME_CHOICES, verbose_name='Prefers a home without (optional)')

    notes = models.TextField(max_length=255, blank=True, null=True, default='')

    slug = models.SlugField(max_length=50, default='', unique=True)

    # calculating animal's age based on the date of birth
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

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.name, self.species, self.id_number, self.location)

    def save(self, *args, **kwargs):
        """the slug will change every time the name changes"""
        self.slug = slugify(self.id_number)
        super(Animal, self).save(*args, **kwargs)


class Cat(models.Model):
    """A class representing dogs, which inherits from the basic Animal class."""

    id = models.OneToOneField('Animal', primary_key=True, related_name="cat")

    BREED_CHOICES = (
        ('Domestic shorthair/mix', 'Domestic shorthair/mix'),
        ('Persian', 'Persian'),
        ('Siamese', 'Siamese')
    )
    cat_breed = models.CharField(max_length=50, choices=BREED_CHOICES, default='Domestic shorthair/mix')

    COLOR_CHOICES = (
        ('white', 'white'),
        ('black', 'black'),
        ('tabby', 'tabby'),
        ('seal point', 'seal point')
    )

    cat_color = models.CharField(max_length=255, choices=COLOR_CHOICES, default='', blank=True)

    PERSONALITY_CHOICES = (
        ('sociable and outgoing', 'sociable and outgoing'),
        ('a bit shy in the shelter environment', 'a bit shy in the shelter environment')
    )

    cat_personality = models.CharField(max_length=255, choices=PERSONALITY_CHOICES, default='', blank=True)

    def __str__(self):
        return '{}'.format(self.id)


class Dog(models.Model):
    """A class representing dogs, which inherits from the basic Animal class."""

    id = models.OneToOneField('Animal', primary_key=True, related_name="dog")

    BREED_CHOICES = (
        ('Terrier/Mix', 'Terrier/Mix'),
        ('Chihuahua', 'Chihuahua'),
        ('Shepherd/Mix', 'Shepherd/Mix')
    )
    dog_breed = models.CharField(max_length=50, choices=BREED_CHOICES, default='', blank=True)

    SIZE_CHOICES = (
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large')
    )

    size = models.CharField(max_length=50, choices=SIZE_CHOICES, default='', blank=True, null=True)
    weight = models.FloatField(max_length=50, validators=[MinValueValidator(0.0)], null=True, blank=True, default='',
                               verbose_name='Specify weight (optional)')

    COLOR_CHOICES = (
        ('white', 'white'),
        ('black', 'black'),
    )

    dog_color = models.CharField(max_length=255, choices=COLOR_CHOICES, default='', blank=True)

    PERSONALITY_CHOICES = (
        ('sociable and outgoing', 'sociable and outgoing'),
        ('profoundly loyal', 'profoundly loyal')
    )

    dog_personality = models.CharField(max_length=255, choices=PERSONALITY_CHOICES, default='')

    def __str__(self):
        return '{}'.format(self.id)

