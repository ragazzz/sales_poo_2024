from django.forms import ModelForm, FileInput
from app.core.models import Line
from django import forms

class LineForm(ModelForm):
  image = forms.ImageField(required=False, label="Línea logo", widget=FileInput(attrs={
    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
  }))

  class Meta:
    model = Line
    fields = ["description", "image"]
    error_messages = {
      "description": {
        "unique": "Ya existe una línea con este nombre.",
      },
    }
    widgets = {
      "description": forms.TextInput(
        attrs={
          "placeholder": "Ingrese descripción de la linea",
          "id": "id_description",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      )
    }
    labels = {
      "description": "Descripción ",
      "image": "Imagen",
    }

  def clean_description(self):
    description = self.cleaned_data.get("description")
    return description.upper()