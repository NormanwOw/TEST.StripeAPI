import stripe
from django.shortcuts import get_object_or_404

from payment.models import Item, Order
from config import DOMAIN_URL


class PaymentServices:

    @staticmethod
    def get_session(currency: str, name: str, price: int):
        session = stripe.checkout.Session.create(
            success_url=DOMAIN_URL + 'success',
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': currency,
                        'product_data': {
                            'name': name
                        },
                        'unit_amount': price,
                    },
                    'quantity': 1,
                }
            ],
        )
        return session


payment = PaymentServices()
