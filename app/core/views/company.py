from django.urls import reverse_lazy
from app.core.forms.company import CompanyForm
from app.core.models import Company
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class CompanyListView(PermissionMixin,ListViewMixin, ListView):
    template_name = 'core/companies/list.html'
    model = Company
    context_object_name = 'companies'
    permission_required = 'view_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:company_create')
        return context

class CompanyCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'core/companies/form.html'
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('core:company_list')
    permission_required = 'add_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Compañia'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        company = self.object
        messages.success(self.request, f"Éxito al crear la marca {company.name}.")
        return response

class CompanyUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Company
    template_name = 'core/companies/form.html'
    form_class = CompanyForm
    success_url = reverse_lazy('core:company_list')
    permission_required = 'change_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar compañia'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        company = self.object
        messages.success(self.request, f"Éxito al actualizar la compañia {company.name}.")
        return response
    
class CompanyDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Company
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:company_list')
    permission_required = 'delete_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Marca'
        context['description'] = f"¿Desea Eliminar la compañia: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la compañia {self.object.name}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)