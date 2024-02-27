from django.views.generic import DetailView, View, TemplateView, ListView
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from payment.models import Item, Order
from payment.services import payment
from config import settings


class BuyView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if self.request.GET.get('order'):
            order = get_object_or_404(Order, id=pk)
            cur = 'usd'
            name = f'Order {order.id}'
            price = order.get_total_usd_cost()
        else:
            item = get_object_or_404(Item, id=pk)
            cur = item.currency
            name = item.name
            price = int(item.price)

        session = payment.get_session(
            currency=cur,
            name=name,
            price=price*100
        )

        return JsonResponse({'id': session['id']})


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item.html'
    extra_context = {'stripe_pub_key': settings.STRIPE_PUBLISHABLE_KEY}


class OrderView(ListView):
    context_object_name = 'order'
    template_name = 'order.html'
    extra_context = {'stripe_pub_key': settings.STRIPE_PUBLISHABLE_KEY}

    def get_queryset(self):
        order_id = self.kwargs.get('pk')
        return get_list_or_404(Item, order_id=order_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_id'] = self.kwargs.get('pk')
        return context


class SuccessPaymentView(TemplateView):
    template_name = 'success.html'

