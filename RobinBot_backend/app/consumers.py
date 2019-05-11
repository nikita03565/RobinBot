from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

connect=[]
channel_layer = get_channel_layer()
class DataConsumer(WebsocketConsumer):
    def connect(self):
        connect.append(self.scope['headers'][0][1].decode("utf-8"))
        async_to_sync(channel_layer.group_add)("chat", self.channel_name)
        print(connect)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        try:
            print(text_data)
            data = json.loads(text_data)
            async_to_sync(self.channel_layer.group_send)(
                "data",
                {
                    "text": text_data,
                },
            )
            print("end")


        except Exception:
            pass


# TODO: push datafile to next