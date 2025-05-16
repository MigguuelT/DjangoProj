# usuarios/urls.py
from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', RedirectView.as_view(url='/usuarios/login/', permanent=True), name='usuarios_raiz'),
    # Redireciona para /usuarios/login/
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('protegida/', views.pagina_protegida, name='protegida'),
]
