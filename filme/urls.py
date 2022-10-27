from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhefilme

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),
    path('filmes/<int:pk>', Detalhefilme.as_view()),
]