from django.urls import reverse_lazy
from app.security.models import GroupModulePermission
from app.security.forms.groupmodulepermission import GroupModulePermissionForm
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/groupmodulepermission/list.html'
    model = GroupModulePermission
    context_object_name = 'grupomodulopermisos'
    permission_required = 'view_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:groupmodulepermission_create')
        return context
    
class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'security/groupmodulepermission/form.html'
    model = GroupModulePermission
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'add_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar permisos'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        gmp = self.object
        messages.success(self.request, f"Éxito al asignar los permisos al grupo {gmp.group.name}")
        return response

class GroupModulePermissionUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = 'security/groupmodulepermission/form.html'
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'change_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar permisos'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        gmp = self.object
        messages.success(self.request, f"Éxito al actualizar los permisos del grupo {gmp.group.name}")
        return response
    
class GroupModulePermissionDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'delete_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar permisos'
        context['description'] = f"¿Desea eliminar los permisos del grupo: {self.object.group.name}?"
        context['back_url'] = self.success_url
        return context