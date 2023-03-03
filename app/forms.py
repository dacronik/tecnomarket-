from django import forms
from .models import Contacto, Producto


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        # importacion de uno a uno
        # fields = ["nombre", "correo", "tipo_contacto", "mensaje", "avisos"]
        # importar todo
        fields = "__all__"


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }
