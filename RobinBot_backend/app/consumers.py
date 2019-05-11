from channels.generic.websocket import WebsocketConsumer
import json


class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        try:
            print(text_data)
            data = json.loads(text_data)

            self.send(json.dumps(
                {
                    'text': '2020_ok'
                }
            ))
        except Exception:
            pass


# TODO: push datafile to next