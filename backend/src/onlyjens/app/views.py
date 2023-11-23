from django.conf import settings
from onlyjens.app.serializers import CreatePaymentIntentSerializer

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

import stripe


stripe.api_key = settings.STRIPE_SK
stripe.public_key = settings.STRIPE_PK


class CreatePaymentIntentView(GenericAPIView):
    def post(self, request):
        serializer = CreatePaymentIntentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        intent = stripe.PaymentIntent.create(
            amount=int(serializer.validated_data['amount'] * 100),
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=[
                "ideal",
                "bancontact",
                "paypal",
                "card"
            ],
        )

        payment = serializer.save()

        request.session.get('payments', []).append(payment.id)
        
        return Response({
            'clientSecret': intent.client_secret,
            'key': stripe.public_key,
            'payment_id': payment.id,
        })


