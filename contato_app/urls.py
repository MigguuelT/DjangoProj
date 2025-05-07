from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar/', views.enviar_mensagem, name='enviar_mensagem'),
    path('editar/<int:mensagem_id>/', views.editar_mensagem, name='editar_mensagem'),
    path('deletar/<int:mensagem_id>/', views.deletar_mensagem, name='deletar_mensagem'),
]