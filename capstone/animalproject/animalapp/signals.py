from .models import Animal
from django.db.models.signals import post_save
from django.dispatch import receiver


# saving each new animal profile instance into Elasticsearch
@receiver(post_save, sender=Animal)
def index_post(sender, instance, **kwargs):
    instance.indexing()
