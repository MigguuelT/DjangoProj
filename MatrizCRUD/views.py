# seu_app/views.py (Matriz CRUD)
from django.shortcuts import render, redirect
from .models import Cliente
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # <-- Importe Paginator aqui

def home(request):
    clientes_list = Cliente.objects.all().order_by('id') # <-- Pega todos os clientes e os ordena
    paginator = Paginator(clientes_list, 5) # Mostra 5 clientes por página

    page = request.GET.get('page') # Pega o número da página da URL (ex: ?page=2)
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não é um inteiro, entrega a primeira página.
        clientes = paginator.page(1)
    except EmptyPage:
        # Se a página está fora do alcance (ex: 9999), entrega a última página de resultados.
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {"clientes": clientes}) # <-- 'clientes' agora é um objeto Page

def salvar(request):
    # A lógica de salvar permanece a mesma, mas agora redireciona para a home
    # que já terá a paginação.
    var_nome = request.POST.get("nome")
    Cliente.objects.create(nome=var_nome)
    # Após salvar, redireciona para a primeira página da lista de clientes
    return redirect('home') # Melhor redirecionar para a home do que re-renderizar

def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'update.html',{"cliente": cliente})

def update(request, id):
    var_nome = request.POST.get("nome")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = var_nome
    cliente.save()
    return redirect('home')

def delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('home')
