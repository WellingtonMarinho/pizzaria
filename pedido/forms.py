from django import forms
from django.forms.models import inlineformset_factory
from django.forms import BaseFormSet
from pedido.models import Pedido, ItemPedido
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        # fields = ('cliente',)
        exclude = []

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cliente', css="form-group col-md-12 mb-0"),
            ),
        )
        super().__init__(*args, **kwargs)



class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        # fields = ('pedido', 'produto', 'quantidade', 'observacao')
        exclude = ['pedido']

formset = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)

    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('pedido', css="form-group col-md-3 mb-0"),
    #             Column('produto', css="form-group col-md-3 mb-0"),
    #             Column('quantidade', css="form-group col-md-3 mb-0"),
    #             Column('observacao', css="form-group col-md-3 mb-0"),
    #             css_class='form-row'
    #     ),
    #         Submit('submit', 'Salvar')
    #     )
    #     super().__init__(*args, **kwargs)