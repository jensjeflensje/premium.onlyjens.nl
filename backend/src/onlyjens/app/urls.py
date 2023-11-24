from django.urls import path
from . import views

urlpatterns = [
    path('payment-intent', views.CreatePaymentIntentView.as_view()),
    path('check-payment/<int:pk>', views.CheckPaymentIntentView.as_view()),
    path('get-certificate/<int:pk>', views.GetCertificateView.as_view()),
]
