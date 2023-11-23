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
    return resData.clientSecret;
}
