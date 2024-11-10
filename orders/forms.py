from django import forms

from bakery.forms import StyleFormMixin
from orders.models import Order



class OrderCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email']