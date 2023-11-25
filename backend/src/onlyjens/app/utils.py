import requests
from django.conf import settings

def send_webhook(title, description, color):
    r = requests.post(settings.DISCORD_WEBHOOK_URL, json={
        "content": None,
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color,
                "footer": {
                    "text": "premium.onlyjens.nl"
                }
            }
        ]
    })
    if r.status_code != 200:
        print(r.text)