from django.shortcuts import render
from audioApp.models import AudioRecording
import uuid
# Create your views here.


def home(request):

    audio_file_name = str(uuid.uuid1())

    context = {"file_name": "audio_"+audio_file_name[0:10]}

    if request.method == "POST":
        """Save recorded audio blob sent by user."""
        audio_file = request.FILES.get('recorded_audio')

        myObj = AudioRecording(name=audio_file_name, audioFile=audio_file)

        myObj.save()

    return render(request, "index.html", context)
