from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView #ProdutoDetailView,


urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name='lista_produtos'),
    path('produto/crie/', ProdutoCreateView.as_view(), name='produtos_create'),
    path('produto/edit/<int:produto_pk>', ProdutoUpdateView.as_view(), name='produtos_edit'),
    path('produto/delete/<int:produto_pk>', ProdutoDeleteView.as_view(), name='produtos_delete'),
    # path('<slug>', ProdutoDetailView.as_view(), name='produto'),

    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('categoria/edit/<int:categoria_pk>', CategoriaUpdateView.as_view(), name='categoria_edit'),
    path('categoria/crie/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:categoria_pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),

]