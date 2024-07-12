from django.forms import ModelForm
from django import forms
from app.security.models import GroupModulePermission

class GroupModulePermissionForm(forms.ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = ['group','module','permissions']
        widgets = {
            'group': forms.Select(
                attrs={
                    'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
                }
            ),
            'module': forms.Select(
                attrs={
                    'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
                }
            ),
            'permissions': forms.SelectMultiple(
                attrs={
                    'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
                }
            )    
        }
        labels = {
            'group': 'Grupo',
            'module': 'Modulo',
            'permissions': 'Permisos',
        }