# Generated by Django 4.2.7 on 2023-11-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_payment_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
