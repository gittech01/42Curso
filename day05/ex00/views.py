from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import psycopg2

def init(request):
    try:
        # Criação da tabela ex00_movies se ainda não existir
        Movie.objects.all().count()

        return HttpResponse("OK")
    except psycopg2.Error as e:
        return HttpResponse(f"Erro: {e}")
