from django.urls import path

from . import views
urlpatterns = [
    path("", views.estoque, name="estoque"),
    path("<int:id>", views.estoqueID, name="estoqueID"),
    path("produto/", views.produto, name="produto"),
    path("produto/<int:id>", views.produtoID, name="produtoID"),
]