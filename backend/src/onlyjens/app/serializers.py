from onlyjens.app.models import Payment
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CreatePaymentIntentSerializer(serializers.ModelSerializer):
    message = serializers.CharField(allow_blank=True)
    author = serializers.CharField(allow_blank=True)
    amount = serializers.FloatField()

    def validate_amount(self, value):
        if value < 4:  # donation amount should be at least 4 euros
            raise ValidationError('Amount must be at least 4')
        return value
    
    class Meta:
        model = Payment
        fields = (
            'message',
            'author',
            'amount',
        )
