from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=25)
    quant = models.BigIntegerField()
    desc = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
    
class Estoque(models.Model):
    setor = models.CharField(max_length=15)
    corredor = models.BigIntegerField()
    prateleira = models.BigIntegerField()
    produto = models.IntegerField()

    def __str__(self):
        return self.setor
    
class Funcionario(models.Model):
    matricula = models.BigIntegerField()
    nome = models.CharField(max_length=25)
    cargo = models.CharField(max_length=25)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cargaHoraria = models.BigIntegerField()
    folhaDePonto = models.BigIntegerField()
    setor = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    produto = models.CharField(max_length=50)
    quant = models.BigIntegerField()

class Venda(models.Model):
    produto = models.CharField(max_length=50)
    quant = models.BigIntegerField()