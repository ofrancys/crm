from django.shortcuts import render, redirect
from .models import Cliente, Pedido, Produto, Representada
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')
    #return render(request, 'clientes/index.html', context)

def clientes(request):
    clientes=Cliente.objects.all()
    context = {
        'clientes' : clientes,
    }
    return render(request, 'clientes/index.html', context)

def add_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'clientes/add_clientes.html', context)

    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        #import pdb
        #pdb.set_trace()
        #if not cnpj:
        #messages.error(request,'CNPJ é obrigatório')
        #return render(request, 'clientes/add_clientes.html', context)
        razao_social = request.POST['razao_social']
        name = request.POST['name']
        number = request.POST['number']
        date_lastsell = request.POST['date_lastsell']

    Cliente.objects.create(cnpj=cnpj,
                            razao_social=razao_social,
                            name=name,
                            number=number,
                            date_lastsell=date_lastsell)
    #messages.success(request, 'Cliente salvo corretamente')
    return redirect('clientes')

def edit_clientes(request, id):
    cliente=Cliente.objects.get(pk=id)
    context={
        'cliente' : cliente,
        'values' : cliente
    }
    if request.method == 'GET':
        return render(request, 'clientes/edit_clientes.html', context)
    #else:
    #    return render(request, 'clientes/edit_clientes.html', context)

    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        razao_social = request.POST['razao_social']
        name = request.POST['name']
        number = request.POST['number']
        date_lastsell = request.POST['date_lastsell']

    cliente.cnpj=cnpj,
    cliente.razao_social=razao_social,
    cliente.name=name,
    cliente.number=number,
    cliente.date_lastsell=date_lastsell

    cliente.save()
    #messages.success(request, 'Cliente editado corretamente')
    return redirect('clientes')

def delete_clientes(request, id):
    cliente=Cliente.objects.get(pk=id)
    cliente.delete()
    #messages.success(request, 'Cliente excluído corretamente')
    return redirect('clientes')
  
#--------------------------------------------------------------------
def pedidos(request):
    pedidos=Pedido.objects.all()
    context = {
        'pedidos' : pedidos
    }
    return render(request, 'pedidos/index.html', context)

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

    Pedido.objects.create(representada=representada,
                            valor_frete=valor_frete,
                            valor_itens=valor_itens)
    messages.success(request, 'Pedido salvo corretamente')

    return redirect('pedidos')

#---------------------------------------------------------------------
def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request, 'produtos/index.html', context)

def add_produtos(request):
    pedidos = Produto.objects.all()
    context = {
        'produtos' : produtos,
        'values':request.POST
    }
    if request.method == 'GET':
        return render(request, 'produtos/add_produtos.html', context)

    if request.method == 'POST':
        cod = request.POST['cod']
        descricao = request.POST['descricao']
        medida = request.POST['medida']
        quantidade = request.POST['quantidade']
        vlr_un = request.POST['vlr_un']
        vlr_total = request.POST['vlr_total']

    Produto.objects.create(cod=cod,
                            descricao=descricao,
                            medida=medida,
                            quantidade=quantidade,
                            vlr_un=vlr_un,
                            vlr_total=vlr_total)
    messages.success(request, 'Pedido salvo corretamente')

    return redirect('produtos')
#----------------------------------------------------------------------

def representadas(request):
    representadas = Representada.objects.all()
    context = {
        'representadas' : representadas
    }
    return render(request, 'representadas/index.html', context)

def add_representadas(request):
    representadas = Representada.objects.all()
    context = {
        'representadas' : representadas,
        'values':request.POST
    }
    if request.method == 'GET':
        return render(request, 'representadas/add_representadas.html', context)

    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        razao = request.POST['razao']
        contato = request.POST['contato']
        numero = request.POST['numero']
        endereco = request.POST['endereco']

    Produto.objects.create(cnpj=cnpj,
                            razao=razao,
                            contato=contato,
                            numero=numero,
                            endereco=endereco)
    messages.success(request, 'Pedido salvo corretamente')

    return redirect('representadas')