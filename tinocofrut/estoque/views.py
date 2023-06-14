from django.shortcuts import render
from django.http import JsonResponse

class Produto:
    def __init__(self, id, quant, desc, nome, preco, categoria, tipo):
        self.id = id
        self.quant = quant
        self.desc = desc
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.tipo = tipo

    def obterData(self):
        return{
            "id": self.id,
            "quant" : self.quant,
            "desc": self.desc,
            "nome": self.nome,
            "preco": self.preco,
            "categoria": self.categoria,
            "tipo": self.tipo
        }
    

produtoLista = []

produto1 = Produto(
    0,
    15,
    'Para fermentar bolos',
    'Fermento de Bolo',
    5.25,
    'Alimento',
    'Ingrediente'
)

produto2 = Produto(
    1,
    50,
    'Adoçar bebidas',
    'Adoçante',
    2.50,
    'Alimento',
    'Ingrediente de cozinha'
)

produto3 = Produto(
    2,
    100,
    'Ingrediente para adoçar alimentos',
    'Açucar',
    3.00,
    'Alimento',
    'Ingrediente de cozinha'
)

produto4 = Produto(
    3,
    50,
    'Para estudos',
    'Caderno',
    7.00,
    'Papelaria',
    'Anotações'
)

produto5 = Produto(
    4,
    30,
    'Para anotações',
    'Caneta',
    1.00,
    'Papelaria',
    'Escrita'
)

produto6 = Produto(
    5,
    500,
    'Para anotações',
    'Lapis',
    0.50,
    'Papelaria',
    'Escrita'
)

produtoLista.append(produto1)
produtoLista.append(produto2)
produtoLista.append(produto3)
produtoLista.append(produto4)
produtoLista.append(produto5)
produtoLista.append(produto6)

class Estoque:
    def __init__(self, setor, corredor, prateleira, produto):
        self.setor = setor
        self.corredor = corredor
        self.prateleira = prateleira
        self.produto = produto

    def obterData(self):
        return{
            "setor": self.setor,
            "corredor": self.corredor,
            "prateleira": self.prateleira,
            "produto": self.produto.obterData()
        }
    
estoqueLista = []

estoque1 = Estoque('Cozinha', 1, 1, produto1)
estoque2 = Estoque('Cozinha', 1, 2, produto2)
estoque3 = Estoque('Cozinha', 1, 3, produto3)
estoque4 = Estoque('Papelaria', 2, 1, produto4)
estoque5 = Estoque('Papelaria', 2, 2, produto5)
estoque6 = Estoque('Papelaria', 2, 3, produto6)

estoqueLista.append(estoque1)
estoqueLista.append(estoque2)
estoqueLista.append(estoque3)
estoqueLista.append(estoque4)
estoqueLista.append(estoque5)
estoqueLista.append(estoque6)

# Create your views here.
def estoque(request):
    output = []
    for est in estoqueLista:
        output.append(est.obterData())

    return JsonResponse(output, safe=False, content_type="application/json")

def estoqueID(request, id):
    return JsonResponse(estoqueLista[int(id)].obterData(), safe=False, content_type="application/json")

def produto(request, id):
    return JsonResponse(produtoLista[0].obterData(), content_type="application/json")