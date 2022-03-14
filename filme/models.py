from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
LISTA_CATEGORIAS = (
    ("MUSICA", "Música"),
    ("JOGOS", "Jogos"),
    ("EDUCACAO", "Educação"),
)


class Filme(models.Model):
    thumb = models.ImageField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    link = models.URLField(default="http://127.0.0.1:8000/")

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    filmes_visto = models.ManyToManyField('Filme')
