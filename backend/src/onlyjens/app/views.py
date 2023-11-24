from django.conf import settings
from onlyjens.app.serializers import CreatePaymentIntentSerializer, CheckPaymentIntentSerializer
from onlyjens.app.models import Payment
from onlyjens.app.tasks import generate_certificate

from django_q.tasks import async_task
from botocore.exceptions import ClientError
from storages.backends import s3boto3

from rest_framework import generics, permissions, status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response

import stripe


stripe.api_key = settings.STRIPE_SK
stripe.public_key = settings.STRIPE_PK

storage = s3boto3.S3Boto3Storage()

class PaymentOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.id in request.session.get('payments', [])


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

        payment = serializer.save(stripe_id=intent.stripe_id)

        payments = request.session.get('payments', [])
        payments.append(payment.id)
        request.session['payments'] = payments
        
        return Response({
            'clientSecret': intent.client_secret,
            'key': stripe.public_key,
            'payment_id': payment.id,
        })


class BasePaymentIntentView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = CheckPaymentIntentSerializer
    permission_classes = [PaymentOwnerPermission]

    def _verify_payment(self):
        serializer = self.serializer_class(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        payment = self.get_object()
        stripe_id = serializer.validated_data['stripe_id']

        if payment.stripe_id != stripe_id:
            return Response({'error': "The payment id doesn't match the stripe id"},
                            status=status.HTTP_400_BAD_REQUEST)

        intent = stripe.PaymentIntent.retrieve(stripe_id)

        if intent['status'] == 'completed':
            return Response({'error': "The payment wasn't successful"},
                            status=status.HTTP_400_BAD_REQUEST)


class CheckPaymentIntentView(BasePaymentIntentView):
    def get(self, request, pk):
        if response := self._verify_payment():
            return response

        payment = self.get_object()
        payment.paid = True
        payment.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetCertificateView(BasePaymentIntentView):
    def get(self, request, pk):
        if response := self._verify_payment():
            return response

        payment = self.get_object()

        file_key = f"certificate_{payment.id}.png"

        try:
            storage.connection.meta.client.head_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=file_key
            )
            url = storage.connection.meta.client.generate_presigned_url(
                'get_object',
                Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': file_key},
                HttpMethod="GET",
                ExpiresIn=3600
            )
            return Response({"url": url})
        except ClientError as err:
            task = async_task(generate_certificate, payment.id, payment.author, payment.created_at.strftime("%d/%m/%Y"))
            print("task", task)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

