from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
User = get_user_model()

#User 가져올때는 상단에 이렇게 쓰고, get_user_model()을 임포트한다

def login_view(request):
    # POST 요청일 때는
    # authenticate -> login 후 'index'로 redirect
    # 실패시에는 다시 GET요청의 로직으로 이동

    # GET 요청일 때는
    # members/login.html 파일을 보여줌
    # 해당 파일의 form에는 username, password input과 '로그인' 버튼이 있음
    # form은 method POST로 다시 이 view로의 action(빈 값)을 가짐
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('index')
    return render(request,'members/login.html',)

def logout_view(request):
    logout(request)
    # /logout/
    # 문서에서 logout <- django logout 검색
    # GET 요청이든 POST 요청이든 상관없음
    pass

def signup_view(request):
    # username, password, password2가 전달되었다는 가정
    # username이 중복되는지 검사, 존재하지 않으면 유저 생성 후 index로 이동
    # 이외의 경우는 다시 회원가입화면으로 보내기
    context= {
        'errors': []
    }

    # 가입 시 받은 데이터에 문제가 있을 때, 기존 print('내용')이 아니라
    # context['errors]를 채우고
    # 해당 내용을 signup.html 템플릿에서 출력하기
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        is_valud = True
        if User.objects.filter(username=username).exists():
            context['errors'].append('Username already exists!')
            is_valid = False
        if password != password2:
            print('Password does not match!')
            is_valid = False
        if is_valid:
            User.objects.create_user(username=username, password=password)
            return redirect('index')
    return render(request, 'members/signup.html')