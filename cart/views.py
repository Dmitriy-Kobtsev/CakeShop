from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bakery.models import Products
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, pk):
    product_pk = pk
    print(f'pk={product_pk}')
    cart = Cart(request)
    product = get_object_or_404(Products, pk=product_pk)
    print(product)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Products, id=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

