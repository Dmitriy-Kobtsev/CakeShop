from django.db import models


class Category(models.Model):

    name = models.CharField(verbose_name='Название', null=True, blank=True)
    about = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return f'Категория: {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Products(models.Model):
    CAKE = 'cake'
    FROST = 'frost'
    MINI_CAKE = 'mini_cake'

    CHOICE_GROUP = {
        (CAKE, 'cake'),
        (FROST, 'frost'),
        (MINI_CAKE, 'mini_cake'),
    }

    name = models.CharField(max_length=60, verbose_name='Название', null=True, blank='True')
    img = models.ImageField(upload_to='products', verbose_name='Изображение', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', null=True, blank='True')
    weight = models.FloatField(verbose_name='Вес', null=True, blank='True')
    description = models.TextField(verbose_name='Описание', null=True, blank='True')
    content = models.TextField(verbose_name='Состав', null=True, blank=True)
    nutritional_value = models.TextField(verbose_name='Пищевая ценность', null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_filter = models.CharField(max_length=20, choices=CHOICE_GROUP, default=CAKE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return f'{self.product_category} {self.name}'

    class Meta:
        verbose_name = 'продукция'
        verbose_name_plural = 'продукции'
