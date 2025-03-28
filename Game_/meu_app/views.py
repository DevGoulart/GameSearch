from django.shortcuts import render
from .models import Jogo
def catalogo(request):
    query = request.GET.get('q')  # Pega o texto da busca
    if query:
        jogos = Jogo.objects.filter(titulo__icontains=query)
    else:
        jogos = Jogo.objects.all()
    return render(request, 'catalogo.html', {'jogos': jogos})

def detalhe_jogo(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    return render(request, 'detalhe_jogo.html', {'jogo': jogo})

def login(request):
    return render(request, 'login.html')

def sobre(request):
    return render(request, 'sobre.html')

def promocoes(request):
    return render(request, 'promocoes.html')
