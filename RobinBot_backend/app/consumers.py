from channels.generic.websocket import WebsocketConsumer
import json


class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, json_data=None, bytes_data=None):
        try:
            data = json.loads(json_data)
            print(data)
            self.send(json.dumps(
                {
                    'text': '200_ok'
                }
            ))
        except Exception:
            pass


# TODO: push datafile to next