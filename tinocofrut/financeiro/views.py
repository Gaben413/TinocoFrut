from django.shortcuts import render
from django.http import JsonResponse
import json

from database.models import Venda, Compra, Produto
from django.core import serializers

# Create your views here.

#GET
def fiscal(request):
    if request.method == 'GET':
        query_set_C = Compra.objects.all()
        query_serialize_C = serializers.serialize('json', query_set_C)
        resposta_json_C = json.loads(query_serialize_C)

        query_set_V = Venda.objects.all()
        query_serialize_V = serializers.serialize('json', query_set_V)
        resposta_json_V = json.loads(query_serialize_V)

        return JsonResponse({
            "resposta de dados":{
                'Vendas': resposta_json_V,
                'Compras': resposta_json_C
            }
        }, safe=False, content_type="application/json")

#GET
def relatorio_compras(request):
    if request.method == 'GET':
        query_set = Compra.objects.all()
        query_serialize = serializers.serialize('json', query_set)
        resposta_json = json.loads(query_serialize)
        return JsonResponse(
            {
                'relatorio de compras': resposta_json
            }
        )

#GET
def relatorio_vendas(request):
    if request.method == 'GET':
        query_set = Venda.objects.all()
        query_serialize = serializers.serialize('json', query_set)
        resposta_json = json.loads(query_serialize)

        return JsonResponse(
            {
                'relatorio de vendas': resposta_json
            }
        )

#POST
def comprar(request):
    if(request.method == 'POST'):
        try:
            decode_json = request.body.decode('utf-8')
            compra_json = json.loads(decode_json)

            compra = Compra(
                produto=compra_json['produto'],
                quant=compra_json['quant']
            )

            q=Produto.objects.get(nome=compra.produto)

            produto_query = Produto.objects.filter(nome=compra.produto).update(
                quant=q.quant + compra.quant
            )

            compra.save()

            return JsonResponse(
                {
                    'Status': 'Compra Realizada',
                    'compra': compra_json
                }
            )
        except Produto.DoesNotExist:
            return JsonResponse({"Error!": "Product not Found"}, safe=False)
    
#POST
def vender(request):
    if(request.method == 'POST'):
        try:
            decode_json = request.body.decode('utf-8')
            venda_json = json.loads(decode_json)

            venda = Venda(
                produto=venda_json['produto'],
                quant=venda_json['quant']
            )

            q=Produto.objects.get(nome=venda.produto)
            produto_query = Produto.objects.filter(nome=venda.produto).update(
                quant=q.quant - venda.quant
            )

            venda.save()

            return JsonResponse(
                {
                    'Status': 'Venda Realizada',
                    'venda': venda_json
                }
            )
        except Produto.DoesNotExist:
            return JsonResponse({"Error!": "Product not Found"}, safe=False)
    
def Test(request, nome):
    try:
        query_set = Produto.objects.get(nome=nome)
        query_Serialize = serializers.serialize('json', [query_set])
        resposta_json = json.loads(query_Serialize)
        return JsonResponse(resposta_json, safe=False, content_type="application/json")
    except Produto.DoesNotExist as e:
        return JsonResponse(
            {
                "Error!": "Product not Found"
            }, safe=False
        )

    