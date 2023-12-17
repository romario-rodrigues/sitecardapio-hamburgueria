from django.shortcuts import render
from burguer.models import Produto



# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'burguer/home.html', context)

def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'burguer/produtos.html', context)
