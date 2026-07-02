# Todas as funções que eu quero que o meu usuário Admin execute, eu venho aqui e habilito a ele
from django.contrib import admin
from.models import Categoria, Artigo

admin.site.register(Categoria)

@admin.register(Artigo) #* O @... Se chama decoration 
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('categoria', 'data_publicacao')