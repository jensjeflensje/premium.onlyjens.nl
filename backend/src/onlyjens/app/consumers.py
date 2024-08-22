from channels.generic.websocket import JsonWebsocketConsumer

from asgiref.sync import async_to_sync
import channels.layers


channel_layer = channels.layers.get_channel_layer()


def send_to_channel_layer(group_name, data):
    async_to_sync(async_send_to_channel_layer)(group_name, {
        "type": "handle_send",
        "data": data,
    })

async def async_send_to_channel_layer(group_name, data):
    await channel_layer.group_send(
        group_name,
        data
    )


class DonationConsumer(JsonWebsocketConsumer):
    groups = ["donations"]

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        message = content["message"]
        self.send_json(content={"message": message})

    def handle_send(self, data):
        self.send_json(content=data["data"])
