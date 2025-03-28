from django.shortcuts import render
from .models import Jogo

def catalogo(request):
    jogos = Jogo.objects.all()
    return render(request, 'catalogo.html', {'jogos': jogos})

def detalhe_jogo(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    return render(request, 'detalhe_jogo.html', {'jogo': jogo})