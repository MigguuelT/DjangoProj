# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy # <-- Importe reverse_lazy

from .forms import CadastroUsuarioForm, LoginForm

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso! Você foi logado automaticamente.')
            # Redireciona para a página protegida após o cadastro
            return redirect(reverse_lazy('usuarios:protegida')) # <-- AQUI ESTÁ A CORREÇÃO!
        else:
            messages.error(request, 'Erro ao realizar o cadastro. Verifique os campos.')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                # Redireciona para a página protegida após o login
                return redirect(reverse_lazy('usuarios:protegida')) # <-- AQUI ESTÁ A CORREÇÃO!
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
                return render(request, 'usuarios/login.html', {'form': form})
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'usuarios/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'usuarios/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    messages.info(request, 'Logout realizado com sucesso!')
    # Após o logout, você pode redirecionar para a página de login
    # ou para a página inicial (home), como já está.
    return redirect('home')

@login_required
def pagina_protegida(request):
    return render(request, 'usuarios/protegida.html')
