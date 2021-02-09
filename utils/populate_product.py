import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaria.settings')
django.setup()

from produto.models import Produto, Categoria
from random import random, randint, randrange, choices


def criando_categorias():
    categorias = ['Pizza', 'Esfiha', 'Salgado', 'Torta', 'Beirute', 'Sanduíche', 'Refrigerante', 'Suco', 'Sorvete', 'Pastel', 'Porção média', 'Porção grande']

    for cada in categorias:
        categoria = cada
        tamanho = choices(['Pequeno', 'Médio', 'Grande'])

        obj = Categoria.objects.create(categoria=categoria, tamanho=tamanho)
        obj.save()


# criando_categorias()


def criando_produtos():

    produtos = ['calabresa', 'Mussarela', 'Pepperoni', 'Queijo', 'Dois Queijos', 'Três Queijos', 'Frango', 'Bacon',
             'Vegetariano', 'Carne', 'Esfiha', 'Salgado', 'Torta', 'Beirute', 'Sanduíche', 'Refrigerante',
             'Suco', 'Sorvete', 'Pastel',]
    for produto in produtos:
        categoria = Categoria.objects.all()[randint(0, Categoria.objects.count())]
        price = randint(1, 80)

        obj = Produto.objects.create(nome=produto, categoria=categoria, preco=price)
        obj.save()
    print(f'Objetos criados com sucesso!')

criando_produtos()
