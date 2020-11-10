from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password  # 비밀번호 암호화 / 패스워드 체크
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.utils.safestring import mark_safe
import json


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
        user_info = user_model.objects.get(email=login_userid)

        if check_password(login_password, user_info.password):
            login(request, user_info)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def dashboard_view(request):
    return render(request, 'dashboard.html')


def register_view(request):
    if request.method == "GET":
        return render(request, 'registration/register.html')


def lost_view(request):
    return render(request, 'registration/lostpassword.html')


def chatroom_index_view(request):
    return render(request, 'room/index.html')


def chatroom_view(request, room_name):
    return render(request, 'room/room.html', {
        'room_name': mark_safe(json.dumps(room_name))
    })
