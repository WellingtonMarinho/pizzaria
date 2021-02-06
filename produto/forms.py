from django import forms
from .models import Produto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css="form-group col-md-4 mb-0"),
                Column('tipo', css="form-group col-md-4 mb-0"),
                Column('preco', css="form-group col-md-4 mb-0"),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar')
        )
        super().__init__(*args, **kwargs)


    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome
