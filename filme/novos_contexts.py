from .models import Filme

def lista_filmes_recentes(requests):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
    return {"lista_filmes_recentes":lista_filmes}


def lista_filmes_em_alta(requests):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"lista_filmes_em_alta":lista_filmes}
