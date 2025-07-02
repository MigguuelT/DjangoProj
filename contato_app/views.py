from django.shortcuts import render, redirect, get_object_or_404
from .forms import MensagemForm
from .models import Mensagem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    lista_de_mensagens = Mensagem.objects.all().order_by('-data_envio')
    paginator = Paginator(lista_de_mensagens, 6)  # Exibe 10 mensagens por página

    page = request.GET.get('page')
    try:
        mensagens = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, entrega a primeira página.
        mensagens = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do range (maior que o número de páginas,
        # entrega a última página.
        mensagens = paginator.page(paginator.num_pages)

    context = {'mensagens': mensagens}
    return render(request, 'contato_app/index.html', context)


def enviar_mensagem(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MensagemForm()
    return render(request, 'contato_app/enviar_mensagem.html', {'form': form})


def editar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    if request.method == 'POST':
        form = MensagemForm(request.POST, instance=mensagem)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MensagemForm(instance=mensagem)
    return render(request, 'contato_app/editar_mensagem.html', {'form': form, 'mensagem': mensagem})


def deletar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    mensagem.delete()
    return redirect('index')
