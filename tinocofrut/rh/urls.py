from django.urls import path

from . import views

urlpatterns = [
    path("", views.obterFuncionarios, name="rh"),
    path("buscar/<id>", views.obterFuncionariosID, name="buscar_usuario"),
    path('registrar/', views.registrar_usuario, name='cadastro_usuario'),
]