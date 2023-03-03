from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_producto, modificar_producto, eliminar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_producto, name="listar_productos"),
    path('modificar-producto/<id>/',
         modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
]
