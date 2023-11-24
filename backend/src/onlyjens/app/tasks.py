from django.core.files.storage import default_storage
from storages.backends import s3boto3
from PIL import Image, ImageDraw, ImageFont

def generate_certificate(payment_id, name, date):
    storage = s3boto3.S3Boto3Storage()
    with storage.open('certificate.png', 'rb') as file:
        certificate = Image.open(file)
    with storage.open('font.ttf', 'rb') as file:
        font = ImageFont.truetype(file, 48)
        file.seek(0)
        date_font = ImageFont.truetype(file, 24)
    draw = ImageDraw.Draw(certificate)
    _, _, w, h = draw.textbbox((0, 0), name, font=font)
    draw.text((750 - int(w/2), 535 - int(h/2)), name, fill=(44, 41, 35), font=font)

    _, _, w, h = draw.textbbox((0, 0), date, font=date_font)
    draw.text((485 - int(w/2), 815 - int(h/2)), date, fill=(44, 41, 35), font=date_font)

    with storage.open(f'certificate_{payment_id}.png', 'wb') as file:
        certificate.save(file)
