from .models import Animal
import django_filters


class AnimalFilter(django_filters.FilterSet):
    """Filtering search results by gender and location"""

    class Meta:
        model = Animal
        fields = ['gender', 'location', ]