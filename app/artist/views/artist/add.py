from django.shortcuts import redirect, render

from artist.models import Artist



__all__ = ('artist_add',)


def artist_add(request):
    # HTML에 Artist 클래스가 받을 수 있는 모든 input을 구현
    # img_profile은 제외
    # method가 POST면 request.POST에서 해당 데이터 처리
    # 새 Artist 객체를 만들고 artist_list로 이동
    # method가 GET이면 artist_add.html을 표시

    # 1. artist/artist_add.html에 Artist_add다 라는 내용만 표시
    # url, view를 서로 연결
    # artist/add/ URL 사용

    if request.method == 'POST':
        name = request.POST['name']
        Artist.objects.create(
            name=name,
        )
        return redirect('artist:artist-list')
    else:
        return render(request, 'artist/artist_add.html')