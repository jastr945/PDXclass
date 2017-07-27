from django.db import models

def profile_upload_handler(instance, filename):
    return '{name}/{filename}'.format(name=instance.name, filename=filename)