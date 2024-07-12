from django.urls import reverse_lazy
from app.core.forms.iva import IvaForm
from app.core.models import Iva
from app.security.instance.menu_module import MenuModule
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q


class IvaListView(PermissionMixin, ListViewMixin, ListView):
  model = Iva
  template_name = 'core/ivas/list.html'
  context_object_name = 'ivas'
  permission_required = 'view_ivas'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['create_url'] = reverse_lazy('core:iva_create')
    context['query'] = self.request.GET.get('q', '')
    return context


class IvaCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Iva
  form_class = IvaForm
  template_name = 'core/ivas/form.html'
  success_url = reverse_lazy('core:iva_list')
  permission_required = 'add_ivas'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title1'] = 'Crear Iva'
    context['title2'] = 'Iva'
    context['back_url'] = self.success_url
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    iva = self.object
    messages.success(self.request, f"Éxito al crear la Iva {iva.description}.")
    return response


class IvaUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Iva
  form_class = IvaForm
  template_name = 'core/ivas/form.html'
  success_url = reverse_lazy('core:iva_list')
  permission_required = 'change_iva'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title1'] = 'Actualizar Iva'
    context['title2'] = 'Actualizar Datos Del Iva'
    context['back_url'] = self.success_url
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    iva = self.object
    messages.success(self.request, f"Éxito al actualizar el IVA {iva.description}.")
    return response


class IvaDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Iva
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:iva_list')
  permission_required = 'delete_iva'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Eliminar IVA'
    context['description'] = f"¿Desea eliminar el IVA {self.object.description}?"
    context['back_url'] = self.success_url
    return context

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el IVA {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)