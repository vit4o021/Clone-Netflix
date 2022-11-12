from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhefilme, Pesquisafilme

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhefilme.as_view(), name='detalhefilme'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme')
]