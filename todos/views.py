from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todos.models import *
from django.shortcuts import render


# defs para routes (pages)
def home(request):
    
    return render(
        request,
        "todos/index.html",
    )


def browse(request):
    
    return render(
        request,
        "todos/browse.html",
    )


def profile(request):
    
    return render(
        request,
        "todos/profile.html",
    )


def streams(request):
    return render(
        request,
        "todos/streams.html",
    )


def details(request):
    return render(
        request,
        "todos/details.html",
    )
# CRUD PARA A EMPRESA

class TodoListView(ListView):
    model = Empresas
class TodoCreateView(CreateView):
    model = Empresas
    fields = ["id","nome","email", "senha", "jogo", "logo", "desc"]
    success_url = reverse_lazy("PaginaInicial")

class TodoUpdateView(UpdateView):
    model = Empresas
    fields = ["id","nome","email", "senha", "jogo", "logo", "desc"]
    success_url = reverse_lazy("PaginaInicial")

class TodoDeleteView(DeleteView):
    model = Empresas
    success_url = reverse_lazy("listarEmpresas")

# CRUD PARA JOGO

class Selctjogo(ListView):
    model = jogo

class InsertJogos(CreateView):
    model = jogo
    fields = ["id","empresa","nome", "preco", "desc", "foto", "data_lancamento"]
    success_url = reverse_lazy("listarJogo")

class UpdateJogo(UpdateView):
    model = jogo
    fields = ["id","empresa","nome", "preco", "desc", "foto", "data_lancamento"]
    success_url = reverse_lazy("listarJogo")
    
class DeleteJogo(DeleteView):
    model = jogo
    success_url = reverse_lazy("listarJogo")

# ------ CRUD DE USUÁRIO -------

class SelctUsuario(ListView):
    model = usuario
    

class InsertUsuario(CreateView):
    model = usuario
    fields = ["id", "nome", "email", "senha", "foto"]
    success_url = reverse_lazy("listarUser")


class UpdateUsuario(UpdateView):
    model = usuario
    fields = ["id", "nome", "email", "senha", "foto"]
    success_url = reverse_lazy("listarUser")

class DeleteUsuario(DeleteView):
    model = usuario
    success_url = reverse_lazy("listarUser")


# -------- CRUD PARA BIBLIOTECA ---- 

class SelctBiblioteca(ListView):
    model = biblioteca

class InsertBiblioteca(CreateView):
    model = biblioteca
    fields = ["id", "id_jogo", "id_user"]
    success_url = reverse_lazy("listarBiblio")


class UpdateBiblioteca(UpdateView):
    model = biblioteca
    fields = ["id", "id_jogo", "id_user"]
    success_url = reverse_lazy("listarBiblio")

class DeleteBiblioteca(DeleteView):
    model = biblioteca
    success_url = reverse_lazy("listarBiblio")