from django.shortcuts import render
from django.http import JsonResponse

class Produto:
    def __init__(self, nome, quant):
        self.nome = nome
        self.quant = quant

    def obterData(self):
        return{
            "nome": self.nome,
            "quant": self.quant
        }

# Create your views here.
def estoque(request):
    produto = Produto("Banana", 15)

    return JsonResponse(produto.obterData(), safe=False, content_type="application/json")