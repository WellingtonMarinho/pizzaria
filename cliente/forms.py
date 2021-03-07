from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Cliente, Endereco


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'endereco', 'telefone']

    def clean_nome(self):
        pass

    def clean_cpf(self):
        pass

    def clean_telefone(self):
        pass


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf']

    def clean_cep(self):
        pass

    def clean_rua(self):
        pass

    def clean_numero(self):
        pass

    def clean_complemento(self):
        pass

    def clean_bairro(self):
        pass

    def clean_complemento(self):
        pass

    def clean_cidade(self):
        pass

    def clean_uf(self):
        pass