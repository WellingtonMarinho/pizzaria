from django.core.management.base import BaseCommand
from produto.factory import SaborFactory, CategoriaFactory
from cliente.factory import ClienteFactory
from pedido.factory import ItemPedidoFactory, PedidoFactory


class Command(BaseCommand):
    help = 'Popula base de dados'

    def create(self, *args, **kwargs):
        # CategoriaFactory.create_batch(1)
        # SaborFactory.create_batch(1)
        # ClienteFactory.create_batch(10)
        # PedidoFactory.create_batch(150)
        # Todos são ativados a partir do ItemPedidoFactory
        ItemPedidoFactory.create_batch(2000)


    def handle(self, *args, **kwargs):
        self.create()
        print('Banco populado.')
