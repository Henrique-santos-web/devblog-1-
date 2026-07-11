from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .forms import Contatoform
from .models import Artigo, Categoria
from .serializers import ArtigoSerializer, CategoriaSerializer

from django.core.paginator import Paginator

def home(request):

    categoria_selecionada = request.GET.get('categoria')

    categorias = Categoria.objects.all()
    
    if categoria_selecionada:
        noticias = Artigo.objects.filter(categoria__nome__icontains=categoria_selecionada)
    else:
        noticias = Artigo.objects.all()

    busca = request.GET.get('q')

    if busca:
        noticias = noticias.filter(titulo__icontains=busca)

    paginator = Paginator(noticias, 5)

    numero_da_pagina = request.GET.get('page')
    page_onj = paginator.get_page(numero_da_pagina)

    contexto = {
        'lista_artigos': page_onj,
        'lista_categorias': categorias,
        'categoria_selecionada': categoria_selecionada
    }
    
    return render(request, "blog/index.html", contexto)


def sobre_nos(request):
    categorias = Categoria.objects.all()

    contexto = {
        'lista_categorias': categorias
    }

    return render(request, "blog/sobre.html", contexto)

# a view recebe o request e o id que veio da url
def artigo_detalhe(request, id):
    # Pede ao banco: "Me dê o Artigo cujo id seja igual a este da URL"
    # Se não achar, mostra a tela de Erro 404 automaticamente!
    noticia = get_object_or_404(Artigo, id=id)

    contexto = {
        'artigo': noticia
    }

    return render(request, 'blog/artigo_detalhe.html', contexto)



def fale_conosco(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        formulario = Contatoform(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        
    else: formulario = Contatoform()

    contexto = {
        'form': formulario,
        'lista_categorias': categorias
    }

    return render(request, 'blog/contato.html', contexto)



# API_REST #

@api_view(['GET'])
def api_listar_artigo(request):
    artigos = Artigo.objects.all()

    serializer = ArtigoSerializer(artigos, many=True) # many diz pro serializer que vai enviar uma lista pra quem 

    return Response(serializer.data) # response

@api_view(['GET'])
def api_listar_categorias(request):
    categorias = Categoria.objects.all()

    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigo(request):
    serializer = ArtigoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)