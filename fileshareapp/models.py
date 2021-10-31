from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class File_info(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    file = models.FileField(null=True, upload_to='media')
    description = models.CharField(max_length=500, blank=True)
    datetime = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return str(self.title)

    