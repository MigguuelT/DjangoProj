"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),
    path('home/', include('MatrizCRUD.urls')),
    path('contato/', include('contato_app.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('api/', include('pessoas.urls')), # <--- Mudei o prefixo para 'api/' para DRF
    path('pessoas/', include('pessoas.urls_html')), # <--- Adicionei uma nova inclusão para as views HTML
    path('', include('Landing_Page.urls')),  # Inclui as URLs da Landing_Page

]
