from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.

class Advertisement(models.Model):
    content = models.FileField(upload_to = settings.ADVERTISING_ROOT)

    def __str__(self):
        return self.content.name

class FileHandler(models.Model):
    file_to_store = models.FileField(upload_to = settings.MEDIA_ROOT)
    bound_advert = models.ForeignKey(Advertisement, default = 1, on_delete = models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.file_to_store.name.split('/')[-1], Advertisement.objects.get(id = self.bound_advert).str().split('/')[-1])
