from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='home'),
    path('jogo/<int:jogo_id>/', views.detalhe_jogo, name='detalhe_jogo'),
]