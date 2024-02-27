from django.urls import path

from payment import views

app_name = 'payment'

urlpatterns = [
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', views.BuyView.as_view(), name='buy'),
    path('order/<int:pk>/', views.OrderView.as_view(), name='order'),
    path('success/', views.SuccessPaymentView.as_view(), name='success')
]
