from django.shortcuts import render

# Create your views here.


def apresentacao(request):
    return render(request, 'apresentacao.html')


def sobreMim(request):
    context = {
        'pagina_atual': 'sobreMim'
    }

    return render(request, 'sobre_mim.html', context)


def index(request):
    context = {
        'pagina_atual': 'index'
    }
    return render(request, 'index.html', context)


def conteudo(request):
    return render(request, 'conteudo.html')
