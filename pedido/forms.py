from django import forms
from pedido.models import Pedido
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'produto', 'quantidade')
        exclude = ['price']

    # def __init__(self, *args, **kwargs):
    #     self.helper = None
