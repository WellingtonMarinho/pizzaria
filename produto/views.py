from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, RedirectView
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'list.html'
    paginate_by = 10
    context_object_name = 'obj_list'

    def get_queryset(self, **kwargs):
        queryset = Produto.objects.all().order_by('created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProdutoListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Produtos'
        return context


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'forms.html'
    success_url = reverse_lazy('produto-list') # Define que url será apontada após o save()


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'detail.html'
    pk_url_kwarg = 'obj_pk'



class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'forms.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('produto-list')
    pk_url_kwarg = 'obj_pk'



class ProdutoDeleteView(DeleteView):
    model = Produto
    pk_url_kwarg = 'obj_pk'
    success_url = reverse_lazy('produto-list')
    template_name = 'delete.html'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'list.html'
    paginate_by = 10
    context_object_name = 'obj_list'

    def get_queryset(self, **kwargs):
        queryset = Categoria.objects.all().order_by('created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Categorias'
        context['list_title'] = 'Lista de Categorias'
        context['editable'] = False
        context['back_line'] = reverse_lazy('index')
        context['back_button'] = 'Voltar'
        context['home'] = 'Index'
        return context


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'detail.html'
    pk_url_kwarg = 'obj_pk'


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'forms.html'
    success_url = reverse_lazy('categoria-list')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'forms.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria-list')
    pk_url_kwarg = 'obj_pk'


class CategoriaDeleteView(DeleteView):
    model = Categoria
    pk_url_kwarg = 'obj_pk'
    success_url = reverse_lazy('categoria-list')
    template_name = 'delete.html'
