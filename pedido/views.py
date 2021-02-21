from django.shortcuts import render
from django.views.generic import CreateView
from pedido.models import Pedido, ItemPedido
from pedido.forms import PedidoForm, ItemPedidoForm
from django.urls import reverse, reverse_lazy
from django.forms.models import inlineformset_factory

def pedido(request):
    if request.method == "GET":
        form = PedidoForm()
        form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)
        form_itempedido = form_item_pedido_factory()
        context = {
            'form': form,
            'form_itempedido': form_itempedido,
        }
        return render(request, 'forms.html', context)




# class PedidoCreateView(CreateView):
    # model = ItemPedido
    # form_class = ItemPedidoForm
    # template_name = 'forms.html'
    # success_url = reverse_lazy('index')
