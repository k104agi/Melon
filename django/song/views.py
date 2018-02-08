from django.shortcuts import render
from song.models import Song


# song_list 만들기
def song_list(requests):
    songs = Song.objects.all()
    context = {
        'songs' : songs,
    }
    return render(
        requests,
        'song/song_list.html',
        context,
    )