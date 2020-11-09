from django.urls import  path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.register_view, name="register_url"),
    path('logout', LogoutView.as_view(next_page='dashboard'), name="logout"),
    path('found', views.lost_view, name='lostpassword_url')
]
