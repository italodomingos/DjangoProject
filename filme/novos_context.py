from .models import Filme


def filme_destaque(request):

    if Filme.objects.all():
        filme = Filme.objects.order_by('-data_criacao')[0]
        filmes_novos = Filme.objects.order_by('-data_criacao')[:9]

    else:
        filme = None
        filmes_novos = None

    return {'filme_destaque': filme, 'filmes_novos': filmes_novos}

