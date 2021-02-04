import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaria.settings')
django.setup()

from produto.models import Product

from random import random, randint, randrange, choices
def criando_produtos(quantidade):
    typos = ['Pizza', 'Esfiha', 'Salgado', 'Torta', 'Beirute', 'Sanduíche', 'Refrigerante', 'Suco', 'Sorvete', 'Pastel', 'Porção média', 'Porção grande']
    names = ['calabresa', 'Mussarela', 'Pepperoni', 'Queijo', 'Dois Queijos', 'Três Queijos', 'Frango', 'Bacon', 'Vegetariano', 'Carne']
    for people in range(quantidade):
        name = choices(names)[0]
        type = choices(typos)[0]
        price = randint(1, 80)

        obj = Product.objects.create(name=name, type=type, price=price)
        obj.save()
