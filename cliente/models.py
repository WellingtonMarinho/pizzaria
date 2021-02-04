from django.db import models
from core.mixins import BaseModel

class Endereco(models.Model):
    cep = models.CharField(max_length=8, blank=False, null=False)
    rua = models.CharField(max_length=255, blank=False, null=False)
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


    @property
    def rua(self):
        return self.endereco.rua

    @property
    def bairro(self):
        return self.endereco.bairro
