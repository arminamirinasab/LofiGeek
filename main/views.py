from django.shortcuts import render

from .models import Music

def fetch_songs(request):
    context = {}
    try:
        songs = Music.objects.all()
        context['songs'] = songs
    except:
        context['songs'] = ""

    return render(request, 'main/index.html', context)