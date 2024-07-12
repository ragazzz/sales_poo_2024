from django.forms import ModelForm
from app.core.models import Product
from django.utils import timezone
from django import forms
import datetime

class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = ["description", "price", "cost", "stock", "brand", "state", "iva", "categories", "line", "expiration_date", "image"]
    error_messages = {
      "description": {
        "unique": "Ya existe un producto con este nombre.",
      }
    }
    widgets = {
      "description": forms.TextInput(
        attrs={
          "placeholder": "Ingrese descripción del producto",
          "id": "id_description",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "price": forms.TextInput(
        attrs={
          "placeholder": "Ingrese precio del producto",
          "id": "id_price",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "cost": forms.TextInput(
        attrs={
          "placeholder": "Ingrese precio del producto",
          "id": "id_cost",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "stock": forms.TextInput(
        attrs={
          "placeholder": "Ingrese stock del producto",
          "id": "id_stock",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "brand": forms.Select(
        attrs={
          "id": "id_brand",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "state": forms.Select(
        attrs={
          "id": "id_state",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "iva": forms.Select(
        attrs={
          "id": "id_iva",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "categories": forms.SelectMultiple(
        attrs={
          "id": "id_categories",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "line": forms.Select(
        attrs={
          "id": "id_line",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "expiration_date": forms.DateInput(
        attrs={
          "type": "date",
          "id": "id_expiration_date",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      ),
      "image": forms.FileInput(
        attrs={
          "type": "file",
          "id": "id_image",
          "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }
      )
    }
    labels = {
      "description": "Producto",
      "price": "Precio",
      "cost": "Costo",
      "stock": "Stock",
      "brand": "Marca",
      "categories": "Categoría",
      "line": "Línea",
      "expiration_date": "Fecha de vencimiento",
      "image": "Imagen",
      "state": "Estado",
      "iva": "Iva",
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if (
      not self.instance.pk
    ):  # Solo establecer el valor predeterminado si el objeto es nuevo
      self.fields["expiration_date"].initial = (
        (timezone.now() + datetime.timedelta(days=30)).date().isoformat()
      )

  def clean_description(self):
    description = self.cleaned_data.get("description")
    return description.upper()