from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^profile/', views.profile_view, name='profile'),
    url(r'^login/', views.login_view, name="login"),
    url(r'^logout/', views.logout_view, name="logout"),
    url(r'^register/', views.register_view, name="register"),
    url(r'^found', views.lost_view, name='lostpassword'),
    url(r'^room/(?P<room_name>[^/]+)/$', views.chatroom_view, name='room'),
    url(r'^room', views.chatroom_index_view, name='index_room'),

]
