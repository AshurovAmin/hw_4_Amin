from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=30, verbose_name='Email')
    password = models.CharField(max_length=35, verbose_name='Password')


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя клиента')
    card_number = models.IntegerField(verbose_name='Номер карточки')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Worker(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя работника')
    position = models.CharField(max_length=20, verbose_name='Должность')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование ингредиента')
    extra_price = models.DecimalField(max_digits=5, decimal_places=2)


class Food(models.Model):
    name = models.CharField(max_length=255)
    start_price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)

