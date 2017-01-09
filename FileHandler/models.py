from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.

class Advertisement(models.Model):
    content_file = models.CharField(max_length = settings.MAX_FILE_PATH_LENGTH, default = 'cat_advert.html')
    exposition_time = models.SmallIntegerField(default = 2)

    def __str__(self):
        return "id: %d, path: %s, exposition time: %d" % (self.id, self.content_file, self.exposition_time)

class FileHandler(models.Model):
    file_to_store = models.FileField(upload_to = settings.MEDIA_ROOT)
    bound_advert = models.ForeignKey(Advertisement, default = 1, on_delete = models.CASCADE)

    def __str__(self):
        return 'id: %d, file path: %s, respective advert id: %d' % (self.id, self.file_to_store.name, self.bound_advert.id)
