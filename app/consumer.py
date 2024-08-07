import json

from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
    def receive(self, text_data=None, bytes_data=None):
        # json데이터 object 로 변환
        obj = json.loads(text_data)
        print("수신 : ", obj)
        # obj 다시 json으로 변환
        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"],
        })
        self.send(json_string)
