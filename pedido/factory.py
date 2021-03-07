import factory
from factory.django import DjangoModelFactory
from pedido.models import Pedido, ItemPedido
from cliente.factory import ClienteFactory, EnderecoFactory


class PedidoFactory(DjangoModelFactory):
    pass