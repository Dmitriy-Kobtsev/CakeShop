from decimal import Decimal
from django.conf import settings
from bakery.models import Products


class Cart(object):

    def __init__(self, request):
        """Инициализируем корзину"""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity, update_quantity=False):
        """Добавить продукт в корзину или обновить"""

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)
                                     }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как 'измененный', что бы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """Удаление товаров из корзины"""

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор элементов в корзине и получение продуктов из базы данных"""
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Products.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Подсчет количества товаров в корзине"""

        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Подсчет стоимости товаров в корзине"""

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Удаление корзины из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True