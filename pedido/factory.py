from random import randint
import factory
from factory.django import DjangoModelFactory
from pedido.models import Pedido, ItemPedido
from cliente.factory import ClienteFactory
from produto.factory import SaborFactory


class PedidoFactory(DjangoModelFactory):
    cliente = factory.SubFactory(ClienteFactory)

    class Meta:
        model = Pedido


class ItemPedidoFactory(DjangoModelFactory):
    pedido = factory.SubFactory(PedidoFactory)
    produto = factory.SubFactory(SaborFactory)
    quantidade = randint(1, 50)
    observacao = factory.Faker('text', max_nb_chars=20)

    class Meta:
        model = ItemPedido
