from django.conf.urls import url

from chat import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/room/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
