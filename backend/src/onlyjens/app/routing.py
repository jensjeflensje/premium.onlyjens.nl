from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/donations/", consumers.DonationConsumer.as_asgi()),
]