# Tutorial to based: https://felipefrizzo.github.io/post/form-inline/

from django.db import models
from cliente.models import Cliente
from core.mixins import BaseModel
from produto.models import Produto


class Pedido(BaseModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    @property
    def endereco(self):
        return f'Rua: {self.cliente.endereco.rua} {self.cliente.endereco.numero} - {self.cliente.endereco.bairro}'

    def __str__(self):
        return f'Pedido N°: {self.id} - {self.cliente.nome} -- {self.endereco}'

    class Meta:
        ordering = ('-created_at',)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)
    observacao = models.CharField(max_length=30, help_text='Observação', null=True, blank=True)

    @property
    def preco(self):
        return self.produto.preco

    def __str__(self):
        return self.produto.nome
