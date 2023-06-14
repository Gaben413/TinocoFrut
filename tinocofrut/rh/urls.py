from django.urls import path

from . import views

urlpatterns = [
    path("", views.obterFuncionarios, name="rh"),
    path("<id>", views.obterFuncionariosID, name="rhID"),
]