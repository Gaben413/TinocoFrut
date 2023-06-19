from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

#GET
def fiscal(request):
    return JsonResponse({"resposta":'dados'}, safe=False, content_type="application/json")

#GET
def relatorio_compras(request):
    return JsonResponse(
        {
            'relatorio': 'compras'
        }
    )

#GET
def relatorio_vendas(request):
    return JsonResponse(
        {
            'relatorio': 'vendas'
        }
    )

#POST
def comprar(request):
    if(request.method == 'POST'):
        decode_json = request.body.decode('utf-8')
        compra_json = json.loads(decode_json)
        return JsonResponse(
            {
                'Status': 'Compra Realizada',
                'compra': compra_json
            }
        )
    
#POST
def vender(request):
    if(request.method == 'POST'):
        decode_json = request.body.decode('utf-8')
        venda_json = json.loads(decode_json)
        return JsonResponse(
            {
                'Status': 'Venda Realizada',
                'venda': venda_json
            }
        )