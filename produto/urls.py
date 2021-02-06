from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoDetailView, CategoriaListView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista-produtos'),
    path('crie/', ProdutoCreateView.as_view(), name='cria-produtos'),
    path('<slug>', ProdutoDetailView.as_view(), name='cria-produtos'),
    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('crie-categorias/', CategoriaListView.as_view(), name='categorias'),

]