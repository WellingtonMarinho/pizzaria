# Tutorial to based: https://felipefrizzo.github.io/post/form-inline/

from django.db import models
from cliente.models import Cliente, Endereco
from core.mixins import BaseModel
from produto.models import Produto


class Pedido(BaseModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    # quantidade = models.PositiveIntegerField()
    # price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)

    # @property
    # def endereco(self):
    #     return f'Rua: {self.cliente.rua} {self.cliente.numero} - {self.cliente.bairro}'

    def __str__(self):
        return f'Pedido N°: {self.id} - {self.cliente.nome} -- {self.endereco}'

    class Meta:
        ordering = ('-created_at',)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField()

    @property
    def preco(self):
        return self.produto.preco
