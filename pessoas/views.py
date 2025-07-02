# pessoas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from rest_framework import viewsets # Importa viewsets para a API
from .models import Pessoa
from .forms import PessoaForm
from .serializers import PessoaSerializer # Importa o serializer para a API

# View para listar todas as pessoas com paginação (HTML).
def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')

    paginator = Paginator(pessoas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pessoas/lista.html', {'page_obj': page_obj})

# View para adicionar uma nova pessoa (HTML).
def adicionar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa adicionada com sucesso!')
            return redirect('pessoas_html:lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'pessoas/form_pessoa.html', {'form': form, 'title': 'Adicionar Pessoa'})

# View para editar uma pessoa existente (HTML).
def editar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa atualizada com sucesso!')
            return redirect('pessoas_html:lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/form_pessoa.html', {'form': form, 'title': 'Editar Pessoa'})

# View para deletar uma pessoa (HTML).
def deletar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        messages.info(request, 'Pessoa deletada com sucesso!')
        return redirect('pessoas_html:lista_pessoas')
    return render(request, 'pessoas/confirm_delete.html', {'pessoa': pessoa})

# ViewSet para a API RESTful (Django REST Framework).
# Esta classe é usada pelo DefaultRouter em pessoas/urls.py para criar endpoints da API.
class PessoaViewSet(viewsets.ModelViewSet):
    # Define o queryset que o ViewSet usará para buscar objetos.
    queryset = Pessoa.objects.all()
    # Define o serializer que o ViewSet usará para serializar/desserializar dados.
    serializer_class = PessoaSerializer