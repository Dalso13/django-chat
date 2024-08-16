from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from chat.models import Room


class ChatConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""

    def connect(self):
        user = self.scope['user']

        if user.is_authenticated:
            room_pk = self.scope['url_route']['kwargs']['room_pk']
            self.group_name = Room.make_chat_group_name(room_pk=room_pk)
            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name,
            )

            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name,
            )

    def receive_json(self, content, **kwargs):
        user = self.scope['user']

        chat_type = content['type']
        if chat_type == 'chat.message':
            sender = user.username
            message = content['message']
            async_to_sync(self.channel_layer.group_send)(
                self.group_name, {
                    'type': 'chat.message',
                    'sender': sender,
                    'message': message
                }
            )
        else:
            print(f"Invalid chat_type ${chat_type}")

    def chat_message(self, message_dict):
        self.send_json(message_dict)

    def chat_room_deleted(self, message_dict):
        custom_code = 4000
        self.close(code=custom_code)
