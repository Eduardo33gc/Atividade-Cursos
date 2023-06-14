from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Curso(models.Model):
    nome_do_curso = models.CharField(max_length = 150)
    texto = models.TextField()
    data_de_criacao = models.DateField()
    imagem = models.ImageField(upload_to = 'imagens')

    def __str__(self):
        return self.nome_do_curso
