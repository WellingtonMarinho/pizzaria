from django.shortcuts import render, redirect
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
        return render(request, 'pedido/form_pedido.html', context)

    elif request.method == "POST":
        form = PedidoForm(request.POST)
        form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm)
        form_itempedido = form_item_pedido_factory(request.POST)
        if form.is_valid() and form_itempedido.is_valid():
            pedido = form.save()
            form_itempedido.instance = pedido
            form_itempedido.save()
            return redirect(reverse('core:index'))
        else:
            context = {
                'form': form,
                'form_itempedido': form_itempedido
            }
            return render(request, 'pedido/form_pedido.html', context)


class ItemPedidoCreateView(CreateView):
    model = ItemPedido
    form_class = ItemPedidoForm
    template_name = 'pedido/form_pedido.html'
    success_url = reverse_lazy('index')
    object = None

    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        item_pedido_factory = inlineformset_factory(Pedido, ItemPedido,form=ItemPedidoForm, extra=2)
        form_item_pedido = item_pedido_factory()
        return self.render_to_response(
            self.get_context_data(form=form, form_itempedido=form_item_pedido))
