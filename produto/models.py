from django.db import models
from core.mixins import BaseModel


# class Type(BaseModel):
#     _TAMANHO = [
#         (1, 'Pequeno'),
#         (2, 'Médio'),
#         (3, 'Grande')
#     ]
#     type = models.CharField(max_length=255, blank=False, null=False, verbose_name='Tipo')
#     tamanho = models.CharField(max_length=10, choices=_TAMANHO)
#
#     def __str__(self):
#         return str(self.type)

class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    type = models.CharField(max_length=255, verbose_name='Tipo')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')

    def __str__(self):
        return self.name

