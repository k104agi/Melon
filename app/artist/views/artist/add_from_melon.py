from datetime import datetime

import requests
from django.core.files import File
from django.shortcuts import redirect
from io import BytesIO

from crawler.artist import ArtistData
from artist.models import Artist


__all__ = ('artist_add_from_melon',)


def artist_add_from_melon(request):
    """
    (1) POST 요청을 받으면 (artist_id를)

    (2) artist_id를 사용해서
    멜론사이트에 들어가 Artist에 들어갈 상세정보 가져오기

    (3) 실제로 저장할 정보 목록
    artist_id
    name
    real_name
    nationality
    birth_date
    constellation
    blood_type
    intro
    위 목록을 채워서 Artist 정보를 생성, DB에 저장하기
    """
    if request.method == 'POST':

        # 로컬호스트 에러난거, 터미널 내역 보면 QueryDict에 artist_id 있음
        # 근데 로컬호스트에 나오지 않았는데 그건 출력커맨드를 안줬기때문
        # 그래서 아래와 같이 지정
        # artist_id = request.POST['artist_id']
        # return HttpResponse(artist_id)
        artist_id = request.POST['artist_id']
        # 크롤링 코드. 자신이 작성한 크롤러를 사용해서 같은 데이터를 가져오면 됩니다
        Artist.objects.update_or_create_from_melon(artist_id)
        return redirect('artist:artist-list')