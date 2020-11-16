import json
from time import time

from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password  # 비밀번호 암호화 / 패스워드 체크
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe


def index_view(request):
    if not request.user.is_anonymous and request.user.UserStatus:
        favorite = request.user.UserFavorite.replace(" ", "")[1:].split("#")
        user_list = get_user_model().objects.all()
        fav_user_list = dict()
        for user in user_list:
            if user.UserStatus:
                for fav in user.UserFavorite.replace(" ", "").split("#"):
                    for my_fav in favorite:
                        if my_fav == fav:
                            try:
                                fav_user_list[user].append(fav)
                            except KeyError:
                                fav_user_list[user] = [fav]
        request.user.fav_user_list = zip(fav_user_list.keys(), fav_user_list.values())
    return render(request, 'index.html')


def register_view(request):
    if request.method == "GET":
        return render(request, 'registration/register.html')

    elif request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        nickname = request.POST.get('nickname', None)
        student_id = request.POST.get('student_id', None)
        department = request.POST.get('department', None)

        quiz_answer = {'information': '박승유', 'software': '장병철', 'business': '박미정', 'design': '정경미'}
        if (quiz_answer[request.POST.get('department', None)] != request.POST.get('quiz', None)) or (
                quiz_answer[department] not in request.POST.get('quiz', None)):
            return HttpResponse('<script>alert("퀴즈를 틀렸습니다!");location.replace(window.location.href)</script>')

        user_model = get_user_model()
        user = user_model(email=email, password=make_password(password), UserName=nickname, UserStudentId=student_id,
                          UserDepartment=department)

        user.code_number = time()
        user.save(True)
        return redirect('login')


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
                return redirect('../room/', request)
            else:
                return HttpResponse(
                    '<script>alert("아이디 또는 비밀번호를 확인하세요!");location.replace(window.location.href)</script>')
        except ObjectDoesNotExist:
            return HttpResponse('<script>alert("아이디 또는 비밀번호를 확인하세요!");location.replace(window.location.href)</script>')


def logout_view(request):
    logout(request)
    return redirect('/')


def lost_view(request):
    return render(request, 'registration/lostpassword.html')


@login_required()
def profile_view(request):
    if request.method == "GET":
        print(request.user.UserProfile)
        return render(request, 'profile.html')
    elif request.method == "POST":
        print(request.FILES)
        if len(request.FILES) > 0:
            request.user.UserProfile = request.FILES.get('image')
            request.user.save(update_fields=['UserProfile'], force_update=True)
            return redirect('profile')
        else:
            request.user.change_user_information(request)
            return HttpResponse('<script>alert("정보를 성공적으로 수정했습니다!");location.replace(window.location.href)</script>')


@login_required()
def chatroom_index_view(request):
    if request.method == "GET":
        return render(request, 'room/index.html')

    elif request.method == "POST":
        request.user.change_user_channels('+', request.POST.get("UserChannels", None))
        return redirect(request.POST.get("UserChannels", None) + '/')


@login_required()
def chatroom_view(request, room_name):
    return render(request, 'room/room.html', {
        'room_name': mark_safe(json.dumps(room_name))
    })
