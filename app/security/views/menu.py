from django.urls import reverse_lazy
from app.security.models import Menu
from app.security.forms.menu import MenuForm
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class MenuListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/menu/list.html'
    model = Menu
    context_object_name = 'menus'
    permission_required = 'view_menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:menu_create')
        return context
    
class MenuCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'security/menu/form.html'
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy('security:menu_list')
    permission_required = 'add_menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Menu'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al crear el menu {menu.name}.")
        return response

class MenuUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Menu
    template_name = 'security/menu/form.html'
    form_class = MenuForm
    success_url = reverse_lazy('security:menu_list')
    permission_required = 'change_menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Menu'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al actualizar el menu {menu.name}.")
        return response
    
class MenuDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Menu
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:menu_list')
    permission_required = 'delete_menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Menu'
        context['description'] = f"¿Desea Eliminar el menu: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el menu {self.object.name}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)