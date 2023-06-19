from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=25, null=True)
    def _str_(self):
        return self.categoria

class Cursos(models.Model):
    titulo = models.CharField(max_length=25, null=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(null=True)
    imagem = models.ImageField(upload_to='imagens')
    def _str_(self):
        return self.categoria
