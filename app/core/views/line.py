from django.urls import reverse_lazy
from app.core.forms.line import LineForm
from app.core.models import Line
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

class LineListView(PermissionMixin,ListViewMixin, ListView):
    template_name = 'core/lines/list.html'
    model = Line
    context_object_name = 'lines'
    permission_required = 'view_line'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:line_create')
        return context

class LineCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'core/lines/form.html'
    model = Line
    form_class = LineForm
    success_url = reverse_lazy('core:line_list')
    permission_required = 'add_line'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Línea'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        line = self.object
        messages.success(self.request, f"Éxito al crear la línea {line.description}.")
        return response

class LineUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Line
    template_name = 'core/lines/form.html'
    form_class = LineForm
    success_url = reverse_lazy('core:line_list')
    permission_required = 'change_line'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Línea'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        line = self.object
        messages.success(self.request, f"Éxito al actualizar la línea {line.description}.")
        return response
    
class LineDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Line
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:line_list')
    permission_required = 'delete_line'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar línea'
        context['description'] = f"¿Desea Eliminar la línea: {self.object.description}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la línea {self.object.description}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)