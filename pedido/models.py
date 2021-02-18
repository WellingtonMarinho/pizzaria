# Tutorial to based: https://felipefrizzo.github.io/post/form-inline/

from django.db import models
from cliente.models import Cliente
from core.mixins import BaseModel
from produto.models import Produto



class Pedido(BaseModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

