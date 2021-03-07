from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Cliente, Endereco


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'endereco', 'telefone']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css="form-group col-md-3 mb-0"),
                Column('cpf', css="form-group col-md-3 mb-0"),
                Column('endereco', css="form-group col-md-3 mb-0"),
                Column('telefone', css="form-group col-md-3 mb-0"),
                css_class='form-class'
            ),
            Submit('submit', 'Salvar')
        )
        super().__init__(*args, **kwargs)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        raise ValidationError('O campo "nome" precisa ser um campo alfabético.') if not nome.isalpha() else nome


    def clean_cpf(self):
        pass

    def clean_telefone(self):
        pass


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cep', css="form-group col-md-4 mb-0"),
                Column('rua', css="form-group col-md-4 mb-0"),
                Column('numero', css="form-group col-md-4 mb-0"),
                Column('complemento', css="form-group col-md-4 mb-0"),
                Column('bairro', css="form-group col-md-4 mb-0"),
                Column('cidade', css="form-group col-md-4 mb-0"),
                Column('uf', css="form-group col-md-4 mb-0"),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar')
        )
        super().__init__(*args, **kwargs)

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