from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
class Funcionario:
    def __init__(self, nome, cargo, salario, cargaHoraria, folhaDePonto, setor):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.cargaHoraria = cargaHoraria
        self.folhaDePonto = folhaDePonto
        self.setor = setor

    def obterData(self):
        return{
            "nome": self.nome,
            "cargo": self.cargo,
            "salario": self.salario,
            "cargaHoraria": self.cargaHoraria,
            "folhaDePonto": self.folhaDePonto,
            "setor": self.setor
        }
    
funcionariosLista = []

funcionario1 = Funcionario('Carlos Mangos', 'Vendas', 2500.00, 8, 5, 'Setor de Vendas')
funcionario2 = Funcionario('Maria Carla', 'Gerenciamento', 3500.00, 10, 15, 'Setor de Gerenciamento')
funcionario3 = Funcionario('Mario Mario', 'Recursos Humanos', 1500.00, 4, 3, 'Recursos Humanos')

funcionariosLista.append(funcionario1)
funcionariosLista.append(funcionario2)
funcionariosLista.append(funcionario3)

def obterFuncionarios(request):
    output = []
    for func in funcionariosLista:
        output.append(func.obterData())
    return JsonResponse(output, safe=False, content_type="application/json")

def obterFuncionariosID(request, id):
    return JsonResponse(funcionariosLista[int(id)].obterData(), safe=False, content_type="application/json")

def registrar_usuario(request):
    if(request.method == 'POST'):
        decode_json = request.body.decode('utf-8')
        registra_usuario = json.loads(decode_json)
        return JsonResponse({
            'Status': 'Cadastro Realizado',
            'registro': registra_usuario
        })