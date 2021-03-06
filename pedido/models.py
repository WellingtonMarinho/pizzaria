# Tutorial to based: https://felipefrizzo.github.io/post/form-inline/
# Tutorial para analisar: https://www.treinaweb.com.br/blog/relacionamento-1-1-1-n-e-n-n-com-django/


from django.db import models
from cliente.models import Cliente
from core.mixins import BaseModel
from produto.models import Sabor


class Pedido(BaseModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    @property
    def endereco(self):
        return f'Rua: {self.cliente.endereco.rua} {self.cliente.endereco.numero} - {self.cliente.endereco.bairro}'

    @property 
    def nome(self):
        return self.cliente.nome

    def __str__(self):
        return f'Pedido N°: {self.id} - {self.cliente.nome} -- {self.endereco}'

    class Meta:
        ordering = ('-created_at',)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Sabor, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)
    observacao = models.CharField(max_length=30, help_text='Observação', null=True, blank=True)

    @property
    def preco(self):
        return self.produto.preco

    def __str__(self):
        return self.produto.sabor

    # def __len__(self):
    #     return len(self.produto)
    #
    # def __getitem__(self, pos):
    #     return self.produto[pos]