from django.contrib import admin
from database import models

# Register your models here.
admin.site.register(models.Produto)
admin.site.register(models.Estoque)
admin.site.register(models.Funcionario)
admin.site.register(models.Compra)
admin.site.register(models.Venda)