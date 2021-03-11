from random import randint
import factory

from factory.django import DjangoModelFactory
from produto.models import Sabor, Categoria

faker = factory.faker.faker.Faker(['pt_br'])

_CATEGORIAS = ['Pizza', 'Esfiha', 'Torta', 'Beirute', 'Salgado',]
_SABOR = ['Queijo', 'Calabresa', 'Carne', 'Frango', 'Bacon', 'Bauru', 'Cantolês']




class CategoriaFactory(DjangoModelFactory):
    categoria = factory.Iterator(_CATEGORIAS)
    descricao = factory.Faker('text', max_nb_chars=100)

    class Meta:
        model = Categoria


class SaborFactory(DjangoModelFactory):
    sabor = factory.Iterator(_SABOR)
    categoria = factory.SubFactory(CategoriaFactory)
    preco = randint(1, 150)

    class Meta:
        model = Sabor
