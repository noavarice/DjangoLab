from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.

class FileHandler(models.Model):
    file_to_store = models.FileField(upload_to=settings.MEDIA_ROOT)
    date = models.DateTimeField()