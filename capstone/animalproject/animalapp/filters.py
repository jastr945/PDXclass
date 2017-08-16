from .models import Animal
import django_filters
from django_filters import STRICTNESS


class AnimalFilter(django_filters.FilterSet):
    """Filtering search results by gender and location."""

    GENDER_CHOICES = (
        (True, 'male'),
        (False, 'female')
    )

    gender = django_filters.ChoiceFilter(choices=GENDER_CHOICES, empty_label='all genders')

    LOCATION_CHOICES = (
        ('OFOSA shelter', 'OFOSA shelter'),
        ('PetSmart Tanasbourne', 'PetSmart Tanasbourne'),
        ('PetSmart Wilsonville', 'PetSmart Wilsonville'),
        ('PetSmart Cedar Hills', 'PetSmart Cedar Hills'),
        ('PetSmart Hillsboro', 'PetSmart Hillsboro'),
        ('Foster home', 'Foster home')
    )

    location = django_filters.ChoiceFilter(choices=LOCATION_CHOICES, empty_label='all locations')

    class Meta:
        model = Animal
        fields = ['gender', 'location', ]
        strict = STRICTNESS.RETURN_NO_RESULTS
