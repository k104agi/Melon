from django.shortcuts import render
from album.models import Album


# song_list 만들기
def album_list(requests):
    albums = Album.objects.all()
    context = {
        'albums' : albums,
    }
    return render(
        requests,
        'album/album_list.html',
        context,
    )