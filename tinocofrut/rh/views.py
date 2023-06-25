from django.shortcuts import render
from django.http import JsonResponse
import json

from database.models import Funcionario
from django.core import serializers

# Create your views here.
'''
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
'''
#GET
def obterFuncionarios(request):
    if request.method == "GET":
        query_set = Funcionario.objects.all()
        query_Serialize = serializers.serialize('json', query_set)
        resposta_json = json.loads(query_Serialize)
        return JsonResponse(resposta_json, safe=False, content_type="application/json")

#GET
def obterFuncionariosID(request, id):
    if request.method == "GET":
        query_set = Funcionario.objects.get(pk=int(id))
        query_Serialize = serializers.serialize('json', [query_set])
        resposta_json = json.loads(query_Serialize)
        return JsonResponse(resposta_json, safe=False, content_type="application/json")

#POST
def registrar_usuario(request):
    if(request.method == 'POST'):
        decode_json = request.body.decode('utf-8')
        registra_usuario = json.loads(decode_json)
        print(registra_usuario['matricula'])

        
        funcionario = Funcionario(
            matricula=registra_usuario['matricula'],
            nome=registra_usuario['nome'],
            cargo=registra_usuario['cargo'],
            salario=registra_usuario['salario'],
            cargaHoraria=registra_usuario['cargaHoraria'],
            folhaDePonto=registra_usuario['folhaDePonto'],
            setor=registra_usuario['setor'],
        )
        funcionario.save()
        
        return JsonResponse({
            'Status': 'Cadastro Realizado',
            'registro': registra_usuario
        })
    
#PUT
def atualizar_usuario(request, id):
    if request.method == "PUT":
        decode_json = request.body.decode('utf-8')
        registra_usuario = json.loads(decode_json)
        query_set = Funcionario.objects.filter(pk=id).update(
            matricula=registra_usuario['matricula'],
            nome=registra_usuario['nome'],
            cargo=registra_usuario['cargo'],
            salario=registra_usuario['salario'],
            cargaHoraria=registra_usuario['cargaHoraria'],
            folhaDePonto=registra_usuario['folhaDePonto'],
            setor=registra_usuario['setor'],
        )
        '''
        query_set = Funcionario.objects.get(pk=id)
        query_set.matricula = registra_usuario['matricula']
        query_set.nome = registra_usuario['nome']
        query_set.cargo = registra_usuario['cargo']
        query_set.salario = registra_usuario['salario']
        query_set.cargaHoraria = registra_usuario['cargaHoraria']
        query_set.folhaDePonto = registra_usuario['folhaDePonto']
        query_set.setor = registra_usuario['setor']
        query_set.save()
        '''

        query_Serialize = serializers.serialize('json', [Funcionario.objects.get(pk=id)])
        resposta_json = json.loads(query_Serialize)
        return JsonResponse({
            'status': 'Cadastro Atualizado',
            'registro': resposta_json
        })

#DELETE
def deletar_usuario(request, id):
    if request.method == "DELETE":
        query_set = Funcionario.objects.get(pk=int(id))
        query_Serialize = serializers.serialize('json', [query_set])
        resposta_json = {
            "Deleted ID deleted": id,
            "contents": json.loads(query_Serialize)
            }

        Funcionario.objects.filter(pk=id).delete()

        return JsonResponse(resposta_json, safe=False, content_type="application/json")

