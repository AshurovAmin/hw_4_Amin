import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django_asgi_app = get_asgi_application()
from fastfood.models import Client, Worker, Food, Ingredient, Order, User


user_azat = User(email='nikname21@gmail.com', password='defender42')
user_azat.save()
client_azat = Client(name='Азат Соколов', card_number='4147565798789009', user=user_azat)
client_azat.save()

user_altynai = User(email='altywa1998@gmail.com', password='nono34')
user_altynai.save()
worker_altynai = Worker(name='Алтынай Алиева', position='Оператор кассы', user=user_altynai)
worker_altynai.save()

shaverma = Food(name='Шаурма', start_price=50)
shaverma.save()
gamburger = Food(name='Гамбургер', start_price=25)
gamburger.save()

syro = Ingredient(name='Сыр', extra_price=10)
syro.save()
kuritsa = Ingredient(name='Курица', extra_price=70)
kuritsa.save()
govyadina = Ingredient(name='Говядина', extra_price=80)
govyadina.save()
salat = Ingredient(name='Салат', extra_price=15)
salat.save()
fri = Ingredient(name='Фри', extra_price=15)
fri.save()

shaverma.ingredients.add(govyadina, syro, salat, fri)
gamburger.ingredients.add(kuritsa, salat)

order_azat_shaurma = Order(food=shaverma, ingredient=govyadina, client=client_azat, worker=worker_altynai)
order_azat_shaurma.save()

order_azat_gamburger = Order(food=gamburger, ingredient=kuritsa, client=client_azat, worker=worker_altynai)
order_azat_gamburger.save()

summ_shaverma = order_azat_shaurma.food.start_price + sum([ingredient.extra_price for ingredient in order_azat_shaurma.food.ingredients.all()])
print("Стоимость шаурмы: {} сом".format(summ_shaverma))

cost_gamburger = order_azat_gamburger.food.start_price + sum([ingredient.extra_price for ingredient in order_azat_gamburger.food.ingredients.all()])
print("Стоимость гамбургера: {} сом".format(cost_gamburger))

total_cost = summ_shaverma + cost_gamburger
print("Общая стоимость заказа: {} сом".format(total_cost))

