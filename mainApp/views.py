from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def main(request): 
    return HttpResponse("메인 페이지")

def test(request):
    return render(request, "img.html")

def mainIndex(request):
    '''
    print('로그인 한 사용자: ', request.user.username)
    print('로그인 한 사용자 id: ', request.user.id)
    print('로그인 확인: ', request.user.is_active)
    print('관리자인지: ', request.user.is_superuser)
    print('마지막 로그인 날짜: ', request.user.last_login)
    print('이름: ', request.user.first_name)
    print('성: ', request.user.last_name)
    print('이메일: ', request.user.email)
    '''
    return render(request, 'mainApp/mainIndex.html')

def createAccount(request):
    print("User.objects.get(id=1) => ", User.objects.get(id=1))
    print("User.objects.all() => ", User.objects.all())
    print("User.objects.values(id, username) => ", User.objects.values('id', 'username'))
    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST.get("id"),
            password = request.POST.get("password"),
            email = request.POST.get("email"),
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"))
        user.save()
        return redirect('login')
    else:
        return render(request, "registration/register.html")

def userInfo(request, userId):
    userInfo = User.objects.get(id=userId)
    context = {"userInfo": userInfo}
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.last_name = request.POST.get('last_name')
        user.first_name = request.POST.get('first_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect("mainIndex")
    else:
        return render(request, "registration/userInfo.html", context)
