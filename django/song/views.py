from django.http import HttpResponse
from django.shortcuts import render
from song.models import Song


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

    context = {}
    if request.method == 'POST':
        # POST 요청에 전달된 데이터(input요소의 값들)중,
        # name이 'keyword'인 input의 값
        keyword = request.POST['keyword'].strip()
        #strip은 양쪽 공백을 없앤 결과를 나타낸다?

        if keyword:
            # Song 목록 중 title이 keyword를 포함하는 쿼리셋
            songs = Song.objects.filter(title__contains=keyword)
            context['songs'] = songs
        # 만약 method가 POST였다면 context에 'songs'가 채워진 상태
        # GET이면 빈 상태로 render 실행
    return render(request, 'song/song_search.html', context)
