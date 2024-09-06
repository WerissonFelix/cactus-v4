"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from todos.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", adm, name='admPagina'),
    path("Principal", home, name='home'),
    path("details/", details, name='details'),
    path("streams/", streams, name='streams'),
    path("browse/", browse, name='browse'),
    path("profile/", profile, name='profile'),
    path("empresasListar", TodoListView.as_view(), name = 'listarEmpresas'),
    path("empresaAdicionar", TodoCreateView.as_view(), name= 'adicionarEmpresas'),
    path("update/<int:pk>", TodoUpdateView.as_view(), name='atualizarEmpresas'),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name='deletarEmpresas'),
    path("jogoListar", Selctjogo.as_view(), name = 'listarJogo'),
    path("jogoAdicionar", InsertJogos.as_view(), name = 'adicionarJogo'),
    path("updatejogo/<int:pk>", UpdateJogo.as_view(), name= 'atualizarJogo'),
    path("deletejogo/<int:pk>", DeleteJogo.as_view(), name='deletarJogo'),
    path("userListar", SelctUsuario.as_view(), name = 'listarUser'),
    path("userAdicionar", InsertUsuario.as_view(), name='adicionarUser'),
    path("updateUser/<int:pk>", UpdateUsuario.as_view(), name='atualizarUser'),
    path("deleteUser/<int:pk>", DeleteUsuario.as_view(), name='deletarUser'),
    path("biblioListar", SelctBiblioteca.as_view(), name = 'listarBiblio'),
    path("biblioAdicionar", InsertBiblioteca.as_view(), name = 'adicionarBiblio'),
    path("updateBiblio/<int:pk>", UpdateBiblioteca.as_view(), name='atualizarBiblio'),
    path("deleteBiblio/<int:pk>", DeleteBiblioteca.as_view(), name='deletarBiblio'),
]