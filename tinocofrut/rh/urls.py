from django.urls import path

from . import views

urlpatterns = [
    path("", views.obterFuncionarios, name="rh"),
    path("delete/<int:id>", views.deletar_usuario, name="delete_usuario"),
    path("atualizar/<int:id>", views.atualizar_usuario, name="atualizar_usuario"),
    path("buscar/<id>", views.obterFuncionariosID, name="buscar_usuario"),
    path('registrar/', views.registrar_usuario, name='cadastro_usuario'),
]