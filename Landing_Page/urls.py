# Landing_Page/urls.py

from django.urls import path
from . import views

app_name = 'landing_page' # Define o namespace do app

urlpatterns = [
    # URL para a página inicial da landing page
    path('', views.landing_page, name='home'),
    # URL para processar a submissão do formulário de contato
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]

