from django.contrib import admin
from .models import Jogo

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'imagem')  # Mostra esses campos na lista
    search_fields = ('titulo',)  # Adiciona busca por título