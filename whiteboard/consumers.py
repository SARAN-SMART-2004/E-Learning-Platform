# whiteboard/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WhiteboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("whiteboard", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("whiteboard", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "whiteboard",
            {
                "type": "whiteboard_draw",
                "x": data['x'],
                "y": data['y']
            }
        )

    async def whiteboard_draw(self, event):
        x = event['x']
        y = event['y']
        await self.send(text_data=json.dumps({'x': x, 'y': y}))
