import json

from channels.generic.websocket import JsonWebsocketConsumer


class LiveBlogConsumer(JsonWebsocketConsumer):
    groups = ['liveBlog']

    def liveBlog_post_created(self, event_dict):
        self.send_json(event_dict)

    def liveBlog_post_updated(self, event_dict):
        self.send_json(event_dict)

    def liveBlog_post_deleted(self, event_dict):
        self.send_json(event_dict)


class EchoConsumer(JsonWebsocketConsumer):
    def receive_json(self, connect, bytes_data=None, **kwargs):
        print("수신 :", connect)
        self.send_json(connect)
