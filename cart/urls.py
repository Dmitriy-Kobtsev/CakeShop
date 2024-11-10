from django.urls import path

from . import views
from .apps import CartConfig

app_name = CartConfig.name

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>/', views.cart_add, name='cart_add'),
    path('remove/<int:pk>/', views.cart_remove, name='cart_remove'),
]