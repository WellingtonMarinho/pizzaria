from django.db import models
from core.mixins import BaseModel
from django.utils.text import slugify


class Categoria(BaseModel):
    categoria = models.CharField(max_length=255, blank=False, null=False, verbose_name='Categoria')
    descricao = models.CharField(max_length=100, )

    def __str__(self):
        return str(self.categoria)


class Produto(BaseModel):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')

    # slug = models.SlugField(unique=True, blank=True, null=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = f'{slugify(self.nome)}'
    #
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
