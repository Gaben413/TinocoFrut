from django.urls import path

from . import views
urlpatterns = [
    path("", views.estoque, name="estoque"),
    path("<int:id>", views.estoqueID, name="estoqueID"),
    path("produto/<int:id>", views.produto, name="produto"),
]