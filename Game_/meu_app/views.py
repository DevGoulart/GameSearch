from django.shortcuts import render, redirect
from .models import Jogo
from django.contrib.auth import authenticate, login as auth_login

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('catalogo')  # Redireciona para o catálogo após login
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'login.html', {})

def login(request):
    return render(request, 'login.html')

def sobre(request):
    return render(request, 'sobre.html')

def promocoes(request):
    return render(request, 'promocoes.html')
