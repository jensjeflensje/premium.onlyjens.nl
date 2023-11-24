import Donation from "@/types/Donation";
import { loadStripe } from '@stripe/stripe-js/pure';

export const stripe = await loadStripe(import.meta.env.VITE_STRIPE_PK);
export const BASE_URL = import.meta.env.VITE_APP_URL;

export async function createPaymentIntent(donation: Donation) : Promise<string> {
    const res = await fetch('/api/payment-intent', {
        method: 'POST',
        body: JSON.stringify(donation),
        headers: {
            'Content-Type': 'application/json',
        },
    });
    const resData = await res.json();
    localStorage.setItem('currentPayment', resData.payment_id);
    return resData.clientSecret;
}

export async function checkPaymentIntent() : Promise<void> {
    await fetch(
        `/api/check-payment/${localStorage.getItem('currentPayment')}?stripe_id=${localStorage.getItem('currentStripeId')}`);
}

export async function getCertificate() : Promise<string | null> {
    const res = await fetch(
        `/api/get-certificate/${localStorage.getItem('currentPayment')}?stripe_id=${localStorage.getItem('currentStripeId')}`);
    if (res.status !== 200) return null;
    const resData = await res.json();
    return resData.url;
}
