from django.urls import reverse_lazy
from app.security.models import Module, GroupModulePermission
from app.security.forms.module import ModuleForm
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class ModuleListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/modules/list.html'
    model = Module
    context_object_name = 'modules'
    permission_required = 'view_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modules_in_use = list(GroupModulePermission.objects.values_list('module_id', flat=True))
        context['create_url'] = reverse_lazy('security:module_create')
        context['modules_in_use'] = modules_in_use
        return context
    
class ModuleCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'security/modules/form.html'
    model = Module
    form_class = ModuleForm
    success_url = reverse_lazy('security:module_list')
    permission_required = 'add_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Módulo'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        module = self.object
        messages.success(self.request, f"Éxito al crear el módulo {module.description}.")
        return response

class ModuleUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Module
    template_name = 'security/modules/form.html'
    form_class = ModuleForm
    success_url = reverse_lazy('security:module_list')
    permission_required = 'change_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Módulo'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        module = self.object
        messages.success(self.request, f"Éxito al actualizar el módulo {module.description}.")
        return response
    
class ModuleDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Module
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:module_list')
    permission_required = 'delete_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Módulo'
        context['description'] = f"¿Desea Eliminar el módulo: {self.object.description}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar el módulo {self.object.description}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)