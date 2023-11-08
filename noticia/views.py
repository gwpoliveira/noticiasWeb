from django.shortcuts import render, redirect 
from django.urls import reverse
from .models import Autor
from .forms import AutorForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class HomeTempleteView(TemplateView):
    template_name = 'home.html'
# Create your views here.

class AutorListView(ListView):
    model = Autor
    template_name = 'listar.html'
    context_object_name = 'autores'
    ordering='-nome'
    
class AutoDetailView(DetailView):
    model=Autor
    template_name = 'detalhar.html'
    context_object_name = 'autor'
    pk_url_kwarg ='id'
    
class AutorCreateView(CreateView):
    model=Autor
    template_name='cadastrar.html'
    form_class=AutorForm
    
    def get_success_url(self):
        messages.success(self.request,"Autor cadastradado com sucesso")
        return reverse('listar')
    
class AutorUpdateView(UpdateView):
    model=Autor
    template_name = 'atualizar.html'
    form_class = AutorForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.success(self.request,"Autor atualizado com sucesso")
        return reverse('listar')


class AutorDeleteView(DeleteView):
    model=Autor
    template_name='autor_confirm_delete.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor deletado com sucesso!")
        return reverse('listar')