from django.forms import ModelForm
from app.core.models import Iva
from django import forms

class IvaForm(ModelForm):
  class Meta:
    model = Iva
    fields = ["description", "value", "image"]
    error_messages = {
      "description": {
        "unique": "Ya existe un Iva con esta descripción.",
      },
    }
    widgets = {
      "description": forms.TextInput(
        attrs={
          "placeholder": "Ingrese descripción del Iva",
          "id": "id_description",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "value": forms.NumberInput(
        attrs={
          "placeholder": "Ingrese Porcentaje",
          "min":"0",
          "max":"15",
          "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        },
      ),
      "image": forms.FileInput(
        attrs={
          "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        },
      )
    }
    labels = {
      "description": "Descripción ",
      "value":"Porcentaje",
      "image": "Imagen",
    }

  def clean_description(self):
    description = self.cleaned_data.get("description")
    return description.upper()