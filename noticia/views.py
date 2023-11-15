from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Autor, Noticia
from .forms import AutorForm, NoticiaForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class HomeTempleteView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.all()[:5]
        context["autores"] = Autor.objects.all()[:5]
        
        return context


class AutorListView(ListView):
    model=Autor
    template_name='autor/listar.html'
    context_object_name='autores'
    ordering='-nome'



class AutorDetailView(DetailView):
    model=Autor
    template_name='autor/detalhar.html'
    context_object_name='autor'
    pk_url_kwarg='id'

class AutorCreateView(CreateView):
    model=Autor
    template_name='autor/cadastrar.html'
    form_class=AutorForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor cadastrado com sucesso!")
        return reverse('listar-autor')
    
class AutorUpdateView(UpdateView):
    model=Autor
    template_name='autor/atualizar.html'
    form_class=AutorForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor atualizado com sucesso!")
        return reverse('listar-autor')

class AutorDeleteView(DeleteView):
    model=Autor
    template_name='autor/autor_confirm_delete.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor deletado com sucesso!")
        return reverse('listar-autor')

class NoticiaListView(ListView):
    model=Noticia
    template_name='noticia/listar.html'
    context_object_name='noticias'
    ordering='-titulo'


class NoticiaDetailView(DetailView):
    model=Noticia
    template_name='noticia/detalhar.html'
    context_object_name='noticia'


class NoticiaCreateView(CreateView):
    model=Noticia
    template_name='noticia/cadastrar.html'
    form_class=NoticiaForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia cadastrada com sucesso!")
        return reverse('listar-noticia')
    

class NoticiaUpdateView(UpdateView):
    model=Noticia
    template_name='noticia/atualizar.html'
    form_class=NoticiaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia atualizada com sucesso!")
        return reverse('listar-noticia')
    

class NoticiaDeleteView(DeleteView):
    model=Noticia
    template_name='noticia/noticia_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia deletada com sucesso!")
        return reverse('listar-noticia')