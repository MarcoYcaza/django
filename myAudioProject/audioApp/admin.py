from django.contrib import admin
from audioApp.models import AudioRecording

# Register your models here.


class AudioRecordingAdmin(admin.ModelAdmin):
    fields = ('name', 'audioFile',)


admin.site.register(AudioRecording, AudioRecordingAdmin)
