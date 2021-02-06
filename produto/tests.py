from django.test import TestCase
from .forms import ProdutoForm


class test_produtoform(TestCase):
    def test_validate_name(self):
        form = ProdutoForm()

        self.assertEqual('Wellington Marinho', form.cleaned_data['nome'])

