from django.urls import reverse_lazy
from app.core.forms.customer import CustomerForm
from app.core.models import Customer
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class CustomerListView(PermissionMixin,ListViewMixin, ListView):
    template_name = 'core/customers/list.html'
    model = Customer
    context_object_name = 'customers'
    permission_required = 'view_brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:customer_create')
        return context

class CustomerCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'core/customers/form.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('core:customer_list')
    permission_required = 'add_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Cliente'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        customer = self.object
        messages.success(self.request, f"Éxito al crear el cliente {customer.first_name}.")
        return response

class CustomerUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Customer
    template_name = 'core/customers/form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('core:customer_list')
    permission_required = 'change_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Cliente'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        customer = self.object
        messages.success(self.request, f"Éxito al actualizar el cliente {customer.first_name}.")
        return response
    
class CustomerDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Customer
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:customer_list')
    permission_required = 'delete_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Cliente'
        context['description'] = f"¿Desea Eliminar el cliente: {self.object.first_name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el cliente {self.object.first_name}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)