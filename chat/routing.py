from django.urls import path

from chat.consumer import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<str:room_pk>/chat/", ChatConsumer.as_asgi()),
]