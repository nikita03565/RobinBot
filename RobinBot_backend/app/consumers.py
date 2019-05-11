from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()


class DataConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(channel_layer.group_add)("data", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        try:
            print(text_data)
            data = json.loads(text_data)

#TODO: some logic





        except Exception:
            pass

    def chat_message(self, event):
        message = event['text']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'text': message
        }))
# TODO: push datafile to next