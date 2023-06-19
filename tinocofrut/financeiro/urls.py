from django.urls import path

from . import views

urlpatterns = [
    path('', views.fiscal, name='dados'),
    path('relatorio/compras/', views.relatorio_compras, name='relatorio_compras'),
    path('relatorio/vendas/', views.relatorio_vendas, name='relatorio_vendas'),
    path('comprar/', views.comprar, name='comprar'),
    path('vender/', views.vender, name='vender')
]