from django.contrib import admin

from .models import Marca, Producto, Contacto


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'precio',
        'descripcion',
        'nuevo',
        'marca',
        'fecha_fabricacion',
        'imagen',
    )
    list_filter = ('nuevo', 'marca', 'fecha_fabricacion')
    list_editable = ['precio']
    search_fields = ['nombre']
    list_per_page = 10


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'correo',
        'tipo_consulta',
        'mensaje',
        'avisos',
    )
    list_filter = ('avisos', 'tipo_consulta')
