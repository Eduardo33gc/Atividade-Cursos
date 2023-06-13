from django.shortcuts import render
from .models import Alimentos,Apicultura,Informatica

# Create your views here.

def index(request):
    context = {'mensagem': 'Conheça os cursos do IFRN - Campus Pau dos Ferros'}
    return render(request, 'core/index.html', context)

def sobre_mim(request):
    context = {'mensagem': 'Conheça mais sobre o desenvolvedor'}
    return render(request, 'core/sobre.html', context)

def lista_alimentos(request):
    postagens = Alimentos.objects.all()
    context = {
        'lista_postagens' : postagens 
    } 
    return render(request,'core/alimentos.html', context)

def lista_apicultura(request):
    postagens = Apicultura.objects.all()
    context = {
        'lista_postagens' : postagens 
    } 
    return render(request,'core/apicultura.html', context)

def lista_informatica(request):
    postagens = Informatica.objects.all()
    context = {
        'lista_postagens' : postagens 
    } 
    return render(request,'core/informatica.html', context)



