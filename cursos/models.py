from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Alimentos(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    data_criacao = models.DateField()
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.titulo

class Apicultura(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    data_criacao = models.DateField()
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.titulo

class Informatica(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    data_criacao = models.DateField()
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.titulo





