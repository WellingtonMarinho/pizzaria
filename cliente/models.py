from django.db import models
from core.mixins import BaseModel


class Endereco(models.Model):
    cep = models.CharField(max_length=8, null=True, blank=True)
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=6, null=False, blank=False, default='Sem número')
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    uf = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.rua


class Cliente(BaseModel):
    nome = models.CharField(max_length=155, null=False, blank=False)
    cpf = models.CharField(max_length=155, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    telefone = models.CharField(max_length=13, blank=False, null=True)

    @property
    def _endereco(self):
        return f'Rua: {self.endereco.rua}, N° {self.endereco.numero} - {self.endereco.bairro}'

    def __str__(self):
        return self.nome
