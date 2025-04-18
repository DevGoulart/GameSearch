from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Jogo
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def catalogo(request):
    query = request.GET.get('q')  # Pega o texto da busca
    if query:
        jogos = Jogo.objects.filter(titulo__icontains=query)
    else:
        jogos = Jogo.objects.all()

    # Configurar a paginação
    paginator = Paginator(jogos, 16)  # Mostrar 9 jogos por página
    page_number = request.GET.get('page')  # Obter o número da página da URL
    page_obj = paginator.get_page(page_number)  # Obter os objetos da página atual

    return render(request, 'catalogo.html', {
        'jogos': page_obj,  # Passar o objeto da página
        'page_obj': page_obj,  # Passar para controle de navegação
        'query': query or ''  # Passar a query para manter a busca
    })

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

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Usuário já existe'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'E-mail já cadastrado'})
        # Cria o novo usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # Faz login automaticamente após o cadastro
        auth_login(request, user)
        return redirect('catalogo')  # Redireciona para o catálogo após cadastro
    return render(request, 'signup.html', {})

def sobre(request):
    return render(request, 'sobre.html')

def promocoes(request):
    return render(request, 'promocoes.html')