import json

from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password  # 비밀번호 암호화 / 패스워드 체크
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        user_model = get_user_model()
        login_userid = request.POST.get('email', None)
        login_password = request.POST.get('password', None)
        try:
            user_info = user_model.objects.get(email=login_userid)
            if check_password(login_password, user_info.password):
                login(request, user_info)
                return render(request, 'room/index.html')
            else:
                return HttpResponse(
                    '<script>alert("아이디 또는 비밀번호를 확인하세요!")\nlocation.replace(window.location.href)</script>')
        except ObjectDoesNotExist:
            return HttpResponse('<script>alert("아이디 또는 비밀번호를 확인하세요!")\nlocation.replace(window.location.href)</script>')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def dashboard_view(request):
    return render(request, 'dashboard.html')


def register_view(request):
    if request.method == "GET":
        return render(request, 'registration/register.html')

    elif request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        nickname = request.POST.get('nickname', None)
        student_id = request.POST.get('student_id', None)
        department = request.POST.get('department', None)

        if request.POST.get('quiz', None) != '박승유':
            return HttpResponse('<script>alert("퀴즈를 틀렸습니다!")\nlocation.replace(window.location.href)</script>')

        user_model = get_user_model()
        user = user_model(email=email, password=make_password(password), UserName=nickname, UserStudentId=student_id,
                          UserDepartment=department)
        user.save()
        return redirect('login')


def lost_view(request):
    return render(request, 'registration/lostpassword.html')


@login_required()
def chatroom_index_view(request):
    return render(request, 'room/index.html')


@login_required()
def chatroom_view(request, room_name):
    return render(request, 'room/room.html', {
        'room_name': mark_safe(json.dumps(room_name))
    })
