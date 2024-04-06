from django.shortcuts import render, redirect
from .models import Cliente, Pedido
from django.contrib import messages
# Create your views here.

def index(request):
    clientes=Cliente.objects.all()
    pedidos=Pedido.objects.all()
    context = {
        'clientes' : clientes,
        'pedidos' : pedidos
    }
    ## fazer retornar os 2 html, um tá desligado pra teste - ambos funcionam
    return render(request, 'pedidos/index.html', context)
    #return render(request, 'clientes/index.html', context)
   
def add_clientes(request):
    return render(request,'clientes/add_clientes.html')
    
    
def add_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes,
        'values':request.POST
    }
    if request.method == 'GET':
        return render(request, 'clientes/add_clientes.html', context)

    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        #import pdb
        #pdb.set_trace()

        if not cnpj:
            messages.error(request,'CNPJ é obrigatório')
            return render(request, 'clientes/add_clientes.html', context)
        razao_social = request.POST['razao_social']
        name = request.POST['name']
        number = request.POST['number']
        date_lastsell = request.POST['date_lastsell']

    
    Cliente.objects.create(cnpj=cnpj,razao_social=razao_social,name=name,
                            number=number,date_lastsell=date_lastsell)
    messages.success(request, 'Cliente salvo corretamente')

    return redirect('clientes')

def add_pedidos(request):
    return render(request,'pedidos/add_pedidos.html')
    

def add_pedidos(request):
    pedidos = Pedido.objects.all()
    context = {
        'pedidos' : pedidos,
        'values':request.POST
    }
    if request.method == 'GET':
        return render(request, 'pedidos/add_pedidos.html', context)

    if request.method == 'POST':
        representada = request.POST['representada']
        valor_frete = request.POST['valor_frete']
        valor_itens = request.POST['valor_itens']

    Pedido.objects.create(representada=representada,valor_frete=valor_frete,valor_itens=valor_itens)
    messages.success(request, 'Pedido salvo corretamente')

    return redirect('pedidos')




