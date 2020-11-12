import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, scope):
        # AsyncConsumer doesn't have __init__ thus there shouldn't be any args
        super().__init__()
        self.scope = scope
        self.room_name = scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

    async def __call__(self, recieve, send):
        # Quick hack, is_double_callable function misses scope argument when
        # calling __call__
        await super().__call__(self.scope, recieve, send)

    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        email = text_data_json['email']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'email': email
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        email = event['email']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'email': email
        }))
