from django.urls import reverse_lazy
from app.core.forms.product import ProductForm
from app.core.models import Product
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class ProductListView(PermissionMixin,ListViewMixin, ListView):
    template_name = 'core/products/list.html'
    model = Product
    context_object_name = 'products'
    permission_required = 'view_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:product_create')
        return context

class ProductCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'core/products/form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('core:product_list')
    permission_required = 'add_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Producto'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        product = self.object
        messages.success(self.request, f"Éxito al crear el producto {product.description}.")
        return response

class ProductUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Product
    template_name = 'core/products/form.html'
    form_class = ProductForm
    success_url = reverse_lazy('core:product_list')
    permission_required = 'change_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Producto'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        product = self.object
        messages.success(self.request, f"Éxito al actualizar el producto: {product.description}.")
        return response
    
class ProductDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Product
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:product_list')
    permission_required = 'delete_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Producto'
        context['description'] = f"¿Desea Eliminar el producto: {self.object.description}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el producto {self.object.description}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)