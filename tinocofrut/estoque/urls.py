from django.urls import path

from . import views
urlpatterns = [
    path("", views.estoque, name="estoque"),
    path("<id>", views.estoqueID, name="estoqueID"),
    path("produto/<id>", views.produto, name="produto"),
]