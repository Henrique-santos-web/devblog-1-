from django.db import models

class Categoria(models.Model):
<<<<<<< HEAD
    #*Aqui estamos colocando o CharField, que serve para usar função max_length, e vai limitar as caracteres (de acordo com o numero que atribuir a ela)
=======
>>>>>>> 42cb02ce311e40ac2bfb61be4ea2752dbb10aa74
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
<<<<<<< HEAD
    #* Sem limite de caracteres
    conteudo = models.TextField()

    #*Preenche com a data/hora exata do cadastro automáticamente
    data_publicacao = models.DateTimeField(auto_now_add=True)

    # O que é o on_delete=models.CASCADE?
    # Define o que acontece com os artigos se a categoria for deletada.
    # CASCADE significa: "deleta a categoria → deleta todos os artigos dela junto". Como um efeito cascata.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #               ↑
    #    esse campo está dentro do Artigo
    #    então é o Artigo que aponta pra Categoria
    #    e não o contrário
    #    Ou seja, por ForeignKey estar dentro de artigo, o ForeignKey pega o artigo e
    #    diz que ele pertence à Categoria
=======
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
>>>>>>> 42cb02ce311e40ac2bfb61be4ea2752dbb10aa74

    autor = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.titulo