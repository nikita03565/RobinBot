from channels.routing import URLRouter
from django.conf.urls import url
from .consumers import DataConsumer

URLRouter([
    url(r"^dataChannel/$", DataConsumer),

])