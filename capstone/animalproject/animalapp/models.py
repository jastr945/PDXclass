from django.db import models
import datetime
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator
from taggit.managers import TaggableManager
from multiselectfield import MultiSelectField
# from .search import AnimalIndex


def upload_pet_image(instance, filename):
    """Images will be uploaded to MEDIA_ROOT/<name>/<filename>"""

    return '{name}/{filename}'.format(name=instance.pet.name, filename=filename)


class Image(models.Model):
    """Image gallery for every pet."""

    img = models.FileField(upload_to=upload_pet_image)
    alt = models.CharField(max_length=255, default='', null=True)
    pet = models.ForeignKey('Animal', related_name='images')


class Animal(models.Model):
    """Contains basic information about each animal, common for cats and dogs."""

    SPECIES_CHOICES = (
        ('', 'Select species...'),
        ('dog', 'dog'),
        ('cat', 'cat')
    )

    species = models.CharField(max_length=50, choices=SPECIES_CHOICES, default='', blank=False)

    name = models.CharField(max_length=50, default='')

    id_number = models.CharField(max_length=50, default='', unique=True)

    gender = models.BooleanField()

    birthday = models.DateField(blank=False, null=False)

    surgery = models.BooleanField(verbose_name='Spayed/neutered')

    vaccine = models.BooleanField(verbose_name='Vaccinated')

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
        ('cats', 'cats'),
        ('dogs', 'dogs'),
        ('other pets', 'other pets'),
        ('young children', 'young children')
    )

    home = MultiSelectField(max_length=255, blank=True, default='', choices=HOME_CHOICES,
                            verbose_name='Prefers a home without (optional)')

    notes = models.TextField(max_length=255, blank=True, null=True, default='')

    tags = TaggableManager()

    slug = models.SlugField(max_length=50, default='', unique=True)

    # calculating animal's age based on the date of birth
    def age(self):
        dob = self.birthday
        tod = datetime.date.today()
        if not dob or not all([dob.year, dob.month, dob.day]):
            return 'no data'
        dob_days = int(dob.year) * 365 + int(dob.month) * 30 + int(dob.day)
        tod_days = int(tod.year) * 365 + int(tod.month) * 30 + int(tod.day)
        age_days = tod_days - dob_days
        animal_year = age_days // 365
        animal_month = (age_days - animal_year * 365) // 30
        animal_day = age_days - animal_year * 365 - animal_month * 30
        return '{}y {}m {}d'.format(animal_year, animal_month, animal_day)

    animal_age = property(age)
    #
    # # adding indexing
    # def indexing(self):
    #    obj = AnimalIndex(
    #       meta={'id': self.id},
    #       breed=self.breed,
    #       intake_date=self.intake_date,
    #       name=self.name,
    #       text=self.text
    #    )
    #    obj.save()
    #    return obj.to_dict(include_meta=True)

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
        ('American Shorthair', 'American Shorthair'),
        ('Birman', 'Birman'),
        ('Domestic Shorthair/Mix', 'Domestic Shorthair/Mix'),
        ('Maine Coon', 'Maine Coon'),
        ('Oriental', 'Oriental'),
        ('Persian', 'Persian'),
        ('Ragdoll', 'Ragdoll'),
        ('Siamese', 'Siamese'),
        ('Siamese/Mix', 'Siamese/Mix'),
        ('Sphynx', 'Sphynx')
    )

    cat_breed = models.CharField(max_length=50, choices=BREED_CHOICES, default='Domestic Shorthair/Mix')

    COLOR_CHOICES = (
        ('black', 'black'),
        ('brown', 'brown'),
        ('calico', 'calico'),
        ('gray', 'gray'),
        ('orange', 'orange'),
        ('seal point', 'seal point'),
        ('tabby', 'tabby'),
        ('tabby orange', 'tabby orange'),
        ('tabby white', 'tabby white'),
        ('tortoiseshell', 'tortoiseshell'),
        ('tuxedo', 'tuxedo'),
        ('white', 'white'),
    )

    cat_color = models.CharField(max_length=255, choices=COLOR_CHOICES, default='', blank=True)

    PERSONALITY_CHOICES = (
        ('very playful', 'very playful'),
        ('sociable and outgoing', 'sociable and outgoing'),
        ('cuddly and affectionate', 'cuddly and affectionate'),
        ('independent', 'independent'),
        ('calm', 'calm'),
        ('a bit shy in the shelter environment', 'a bit shy in the shelter environment'),
        ('loves to be around people', 'loves to be around people'),
        ('adores brushing', 'adores brushing'),
        ('needs a quiet home', 'needs a quiet home'),
        ('needs love and consistency', 'needs love and consistency'),
        ('appreciates lots of attention', 'appreciates lots of attention'),
        ('talkative', 'talkative'),
        ('not shy about looking for attention', 'not shy about looking for attention'),
        ('sweet and gentle', 'sweet and gentle')
    )

    cat_personality = MultiSelectField(choices=PERSONALITY_CHOICES, default='', blank=True)

    def __str__(self):
        return '{}'.format(self.id)


class Dog(models.Model):
    """A class representing dogs, which inherits from the basic Animal class."""

    id = models.OneToOneField('Animal', primary_key=True, related_name="dog")

    BREED_CHOICES = (
        ('Beagle', 'Beagle'),
        ('Boxer', 'Boxer'),
        ('Bulldog', 'Bulldog'),
        ('Chihuahua', 'Chihuahua'),
        ('Dachshund', 'Dachshund'),
        ('German Shepherd', 'German Shepherd'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Labrador Retriever', 'Labrador Retriever'),
        ('Labrador/Mix', 'Labrador/Mix'),
        ('Miniature Schnauzer', 'Miniature Schnauzer'),
        ('Poodle', 'Poodle'),
        ('Shepherd/Mix', 'Shepherd/Mix'),
        ('Shih Tzu', 'Shih Tzu'),
        ('Spaniel/Mix', 'Spaniel/Mix'),
        ('Terrier/Mix', 'Terrier/Mix'),
        ('Yorkshire Terrier', 'Yorkshire Terrier')
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
        ('black', 'black'),
        ('brown', 'brown'),
        ('tan', 'tan'),
        ('white', 'white')
    )

    dog_color = MultiSelectField(choices=COLOR_CHOICES, default='', blank=True)

    PERSONALITY_CHOICES = (
        ('friendly and affectionate', 'friendly and affectionate'),
        ('sociable and outgoing', 'sociable and outgoing'),
        ('profoundly loyal', 'profoundly loyal'),
        ('house-trained', 'house-trained'),
        ('cuddly and affectionate', 'cuddly and affectionate'),
        ('frequent training sessions', 'frequent training sessions'),
        ('friendly toward strangers', 'friendly toward strangers'),
        ('has a quiet, laid-back temperament', 'has a quiet, laid-back temperament'),
        ('loves running around and playing', 'loves running around and playing'),
        ('not very fond of the outdoors', 'not very fond of the outdoors')
    )

    dog_personality = MultiSelectField(choices=PERSONALITY_CHOICES, default='', blank=True)

    def __str__(self):
        return '{}'.format(self.id)
