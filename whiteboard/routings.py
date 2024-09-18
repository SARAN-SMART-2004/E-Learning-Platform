# whiteboard/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/whiteboard/', consumers.WhiteboardConsumer.as_asgi()),
]
