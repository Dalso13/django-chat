from django.urls import path

from app.consumer import EchoConsumer, LiveBlogConsumer

websocket_urlpatterns = [
    path("ws/echo/", EchoConsumer.as_asgi()),
    path("ws/live-blog/", LiveBlogConsumer.as_asgi()),

]
