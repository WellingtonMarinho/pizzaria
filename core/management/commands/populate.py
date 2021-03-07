from django.core.management.base import BaseCommand
from produto.factory import ProdutoFactory, CategoriaFactory
from cliente.factory import ClienteFactory

class Command(BaseCommand):
    help = 'Popula base de dados'

    def create(self, *args, **kwargs):
        # CategoriaFactory.create_batch(1)
        # ProdutoFactory.create_batch(1)
        # ClienteFactory.create_batch(10)
        ...


    def handle(self, *args, **kwargs):
        self.create()
        print('Banco populado.')
