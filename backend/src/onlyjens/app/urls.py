from django.urls import path
from . import views

urlpatterns = [
    path('payment-intent', views.CreatePaymentIntentView.as_view()),
]
