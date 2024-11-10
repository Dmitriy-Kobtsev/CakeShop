from . import views
from django.urls import path
from .apps import OrdersConfig

app_name = OrdersConfig.name

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]