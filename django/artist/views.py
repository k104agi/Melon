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
        pass
    else:
        return render(request, 'artist/artist_add.html')

    # 2. artist_add.html에 form을 하나 생성
    # input은 name이 'name'인 요소 한개만 생성
    # POST 방식으로 전송 후, 전달받은 'name' 값을 바로 HttpResponse로 보여주기
