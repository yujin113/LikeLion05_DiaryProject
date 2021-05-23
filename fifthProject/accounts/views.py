from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST': # Sign Up! 버튼 눌렀을 때
        if request.POST['username'] == "":
            return render(request, 'accounts/signup.html', {'error':'The given username must be set'})
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username']) #User에 이미 같은 username이 있으면
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user( # createuser(username, password)
                    request.POST['username'], password=request.POST['password1']
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # Sign Up! 버튼을 누르지 않은 상태 -> User가 정보 입력 중
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST': # 로그인 버튼 눌렀을 때
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: # 사용자 정보를 알맞게 입력한 경우
            auth.login(request, user)
            return redirect('home')
        else: # 사용자 정보가 잘못 입력된 경우
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')