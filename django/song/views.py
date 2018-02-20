from typing import NamedTuple
from django.db.models import Q

from django.shortcuts import render
from .models import Song


# song_list 만들기
def song_list(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(
        request,
        'song/song_list.html',
        context,
    )


def song_search(request):
    """
    (1)
    사용할 URL: song/search/
    사용할 Template: templates/song/song_search.html
        form 안에 input 한 개, button 한 개 배치

    (2)검색기능 구현 - GET, POST 분기
    1. input의 name을 keywod로 지정
    2. 이 함수를 request.method가 'GET'
    3. request.method가 'POST'일 때
    request.POST dict의 keyword 키에 해당하는 값을
    HttpResponse로 출력
    4. request.method가 GET일때 이전에 하던 템플릿 출력을 유지

    (3) Query Filter로 검색하기
    1. keyword가 자신의 title에 포함되는 Song 쿼리셋 생성
    2. 위 쿼리셋을 'songs' 변수에 할당
    3. context dict를 만들고 'songs'키에 songs 변수를 할당
    4. render의 3번째 인수로 context를 전달
    5. template에 전달된 'songs'를 출력
    """

    # Song과 연결된 Artist의 name에 keyword가 포함되는 경우
    # Song과 연결된 Album의 name에 keyword가 포함되는 경우
    # 두 경우를 모두 포함(or -> Q object)하는 쿼리셋을 'songs'에 할당
    # 밑의 Song.objects.filter에 붙은거를 or로 바꾸기
    # Song의 title에 keyword가 포함되는 경우까지 합쳐서 3개를 or로 조건달기
    # 오늘 마지막으로 본 문서 찾아서 만들기

    # if request.method == 'GET':
    # POST 요청에 전달된 데이터(input요소의 값들)중,
    # name이 'keyword'인 input의 값

    # dictionary인 GET내용에서 keyword 가져오기
    context = {
        'song_infos': [],
    }
    keyword = request.GET.get('keyword')

    class SongInfo(NamedTuple):
        type: str
        q: Q

    if keyword:
        song_infos = (
            SongInfo(
                type='아티스트명',
                q=Q(album__artists__name__contains=keyword)),
            SongInfo(
                type='앨범명',
                q=Q(album__title__contains=keyword)),
            SongInfo(
                type='노래제목',
                q=Q(title__name__contains=keyword)),
        )
        for type, q in song_infos:
            context['song_infos'].append({
                'type':type,
                'songs':Song.objects.filter(q),
            })
    return render(request, 'song/song_search.html', context)


            # # Song과 연결된 Artist의 name에 keyword가 포함되는 경우
            # songs_from_artists = Song.objects.filter(
            #     album__artists__name__contains=keyword)
            #
            # # album name에 keyword
            # songs_from_albums = Song.objects.filter(
            #     album__title__contains=keyword)
            #
            # # title name에 keyword
            # songs_from_title = Song.objects.filter(
            #     title__contains=keyword)
            # # 만약 method가 POST였다면 context에 'songs'가 채워진 상태
            # # GET이면 빈 상태로 render 실행
            #
            # # 방법 1
            # # for문 순회하며 append()하는 부분이 한 번만 쓰이도록
            # # zip을 활용
            # # for type, songs in zip(
            # #         ('아티스트', '앨범', '노래제목'),
            # #         (songs_from_artists, songs_from_albums, songs_from_title)):
            # #     context['song_infos'].append({
            # #     'type': type,
            # #     'songs': songs
            # #     })
            #
            # # 방법 2
            # song_infos = (
            #     ('아티스트', songs_from_artists),
            #     ('앨범', songs_from_albums),
            #     ('노래제목', songs_from_title)
            # )
            # for type, songs in song_infos:
            #     context['song_infos'].append({
            #         'type': type,
            #         'songs': songs
            #     })

            # 방법3
            # filter 뒤의 조건을 Q Object로 만들어서 아래 for 문에서 사용하기
            # q = Q(title__contains=keyword)
            # Song.objects.filter(q)

            # if keyword 하의 내용을 다음과 같이 바꿈
            # song_infos = (Q Song.objects.filter(
            #     album__artists__name__contains=keyword)

            # 방법 4
            # namedtuple(네임드튜플) 사용하기
            # class SongInfo(NamedTuple):
            #   type: #str
            #   q: Q
            #     context = {'song_infos': [], }
            #     keyword = request.GET.get('keyword')
            #     SongInfo = namedtuple('SongInfo', ['type', 'q'])
            #
            #     if keyword:
            #         song_infos=(
            #             SongInfo(
            #                 type='아티스트명',
            #                 q=Q(album__artists__name__contains=keyword)),            )
            #             )
            #
            #     for type ~~

            #return render(request, 'song/song_search.html', context)



