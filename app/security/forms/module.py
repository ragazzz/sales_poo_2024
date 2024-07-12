from django.forms import ModelForm
from django import forms
from app.security.models import Module

class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['url', 'name', 'menu', 'description', 'icon', 'permissions']
        error_messages = {
            "name": {
                "unique": "Ya existe un módulo con este nombre."
            }
        }
        widgets = {
            "url": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el url del módulo",
                    "id": "id_url",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del módulo",
                    "id": "id_name",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "menu": forms.Select(
                attrs={
                    "id": "id_menu",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese una descripción al módulo",
                    "id": "id_description",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "icon": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese icono",
                    "id": "id_icon",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "permissions": forms.SelectMultiple(
                attrs={
                    "id": "id_permissions",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            )
        }
        labels = {
            "url": "Url",
            "name": "Nombre del menu",
            "menu": "Menú",
            "description": "Descripción",
            "icon": "Clase del icono",
            "permissions": "Permisos",
        }