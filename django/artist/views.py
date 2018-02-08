from django.shortcuts import render

from artist.models import Artist


def artist_list(requests):
    # 전체 Artist 목록을 ul>li로 출력
    # 템플릿은 'artist/artist_list.html'을 사용
    # 전달할 context 키는 'artists'를 사용
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(
        requests,
        'artist/artist_list.html',
        context,
    )

# album_list 만들기
