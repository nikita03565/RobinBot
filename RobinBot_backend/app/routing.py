from channels.routing import ProtocolTypeRouter

from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url('dataChannel/', consumers.DataConsumer),
]