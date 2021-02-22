from django.views.generic import ListView
from django.urls import reverse_lazy
from produto.models import Categoria


class IndexView(ListView):
    model = Categoria
    template_name = 'index.html'
    paginate_by = 10
    context_object_name = 'obj_list'

    def get_queryset(self, **kwargs):
        queryset = Categoria.objects.all().order_by('-created_at')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page_title'] = 'Home Page'
        context['back_button'] = reverse_lazy
        return context
