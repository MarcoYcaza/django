from django.db import models

# Create your models here.


class AudioRecording(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    audioFile = models.FileField(
        null=True, blank=True, upload_to="my_recordings")

    def __str__(self):
        return self.name
