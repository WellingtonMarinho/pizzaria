from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoDetailView, ProdutoUpdateView, ProdutoDeleteView, \
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, CategoriaDetailView


urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name='produto-list'),
    path('produto/create/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/<int:obj_pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
    path('produto/edit/<int:obj_pk>/', ProdutoUpdateView.as_view(), name='produto-edit'),
    path('produto/delete/<int:obj_pk>/', ProdutoDeleteView.as_view(), name='produto-delete'),
    path('produtos/combos/', ProdutoListView.as_view(), name='lista-combos'), ##### A criar views

    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/create/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/<int:obj_pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categoria/edit/<int:obj_pk>/', CategoriaUpdateView.as_view(), name='categoria-edit'),
    path('categoria/delete/<int:obj_pk>/', CategoriaDeleteView.as_view(), name='categoria-delete'),
]
