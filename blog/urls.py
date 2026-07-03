# Aqui criamos novas URLs ou deixamos elas dinâmicas
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    # a nova URL dinâmica:
    # <int:id> diz: Espere um número inteiro aqui e o chamde de ID
    path('artigo/<int:id>', views.artigo_detalhe, name='detalhe_artigo')
]