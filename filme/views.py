from django.shortcuts import render
from .models import Filme

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def home_filmes(request):
    context = {}
    context['lista_filmes'] = Filme.objects.all()
    return render(request, "home_filmes.html", context)

