from django.conf.urls import url

from chat import chat_consumers, vc_consumers

websocket_urlpatterns = [
    url(r'^ws/chat/room/(?P<room_name>[^/]+)/$', chat_consumers.ChatConsumer),
    url(r'^ws/chat/vc/(?P<room_name>[^/]+)/$', vc_consumers.ChatConsumer),
]
