from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('sobre/', views.sobre, name='sobre'),
    path('promocoes/', views.promocoes, name='promocoes'),
    path('login/', views.login, name='login'),
    path('jogo/<int:jogo_id>/', views.detalhe_jogo, name='detalhe_jogo'),
]
