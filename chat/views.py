from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password  # 비밀번호 암호화 / 패스워드 체크
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    response_data = {}
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        user_model = get_user_model()
        login_userid = request.POST.get('id', None)
        login_password = request.POST.get('password', None)
        user_info = user_model.objects.get(email=login_userid)


        if login_password == user_info.password:
            request.session['user'] = user_info.id
            login(request, user_info)
            return render(request, 'index.html', response_data)
        else:
            response_data['error'] = "비밀번호가 틀렸습니다."
            return render(request, 'login.html', response_data)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def dashboard_view(request):
    return render(request, 'dashboard.html')


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def lost_view(request):
    return render(request, 'registration/lostpassword.html')
