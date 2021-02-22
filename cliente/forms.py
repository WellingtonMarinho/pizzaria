from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Cliente, Endereco


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
