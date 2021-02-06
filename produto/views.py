from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produtos.html'
    paginate_by = 10


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/cria-produto.html'
    success_url = reverse_lazy('lista-produtos') # Define que url será apontada após o save()


class ProdutoDetailView(DetailView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/cria-produto.html'
    pk_url_kwarg = 'slug'
    # success_url = reverse_lazy('cria-produtos')


class CategoriaListView(ListView):
    model = Categoria
    # form_class = CategoriaForm
    template_name = 'produto/categorias.html'
    paginate_by = 10


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produto/cria-categoria.html'
    success_url = reverse_lazy('categorias')