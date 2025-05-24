# pessoas/urls_html.py

from django.urls import path
from . import views

# Define o namespace para as URLs HTML, útil para evitar conflitos de nomes.
app_name = 'pessoas_html'

urlpatterns = [
    # URL para a lista de pessoas.
    path('', views.lista_pessoas, name='lista_pessoas'),
    # URL para adicionar uma nova pessoa.
    path('adicionar/', views.adicionar_pessoa, name='adicionar_pessoa'),
    # URL para editar uma pessoa existente, usando o ID (pk) como parâmetro.
    path('editar/<int:pk>/', views.editar_pessoa, name='editar_pessoa'),
    # URL para deletar uma pessoa existente, usando o ID (pk) como parâmetro.
    path('deletar/<int:pk>/', views.deletar_pessoa, name='deletar_pessoa'),
]
