# Landing_Page/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ContactSubmission
from django.contrib import messages # Para mensagens de sucesso/erro

def landing_page(request):
    """
    Renderiza a página inicial da landing page.
    """
    return render(request, 'Landing_Page/landing_page.html')

def contact_submit(request):
    """
    Processa a submissão do formulário de contato.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Cria e salva a submissão no banco de dados
            ContactSubmission.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.')
            # Redireciona para a própria landing page após a submissão bem-sucedida
            return redirect(reverse('landing_page:home'))
        else:
            messages.error(request, 'Por favor, preencha todos os campos do formulário.')
    # Se não for POST ou se houver erro, redireciona de volta para a landing page
    return redirect(reverse('landing_page:home'))
