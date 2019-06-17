from django.db import models
from main.models import User, Product
from enum import Enum

# Create your models here.

class Status(Enum):
    PROCCESING = 'В обработке'
    SHIPMENT = 'Отправлен'
    CLOSED = 'Закрыт'

    def __str__(self):
        return self.value


class Order(models.Model):
    client = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=50, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True)
    postal_code = models.CharField(verbose_name='Почтовый код', max_length=20, null=True)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True, null=True)
    status = models.CharField(max_length=20, choices=[(status.value, status.name) for status in Status], default=Status.PROCCESING.value)
    paid = models.BooleanField(verbose_name='Оплачен', default=False, null=True)

    def get_total_cost(self):
            return sum(item.get_cost() for item in TempProduct.objects.filter(order=self))

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

class TempProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)
    price = models.PositiveIntegerField(verbose_name="Цена", null=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

