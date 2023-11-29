from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Autor, Noticia
from .forms import AutorForm, NoticiaForm, RegistrationForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class HomeTemplateView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.all()[:5]
        context["autores"] = Autor.objects.all()[:5]
        
        return context




class AutorListView(LoginRequiredMixin, ListView):
    model=Autor
    template_name='autor/listar.html'
    context_object_name='autores'
    ordering='-nome'
    paginate_by = 5


class AutorDetailView(LoginRequiredMixin, DetailView):
    model=Autor
    template_name='autor/detalhar.html'
    context_object_name='autor'
    pk_url_kwarg='id'


class AutorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model=Autor
    template_name='autor/cadastrar.html'
    form_class=AutorForm
    permission_required = 'noticia.add_autor'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor cadastrado com sucesso!")
        return reverse('listar-autor')

class AutorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Autor
    template_name='autor/atualizar.html'
    form_class=AutorForm
    pk_url_kwarg='id'
    permission_required = 'noticia.change_autor'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor atualizado com sucesso!")
        return reverse('listar-autor')

class AutorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model=Autor
    template_name='autor/autor_confirm_delete.html'
    pk_url_kwarg='id'
    permission_required = 'noticia.delete_autor'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor deletado com sucesso!")
        return reverse('listar-autor')

class NoticiaListView(LoginRequiredMixin, ListView):
    model=Noticia
    template_name='noticia/listar.html'
    context_object_name='noticias'
    ordering='-titulo'
    paginate_by = 5


class NoticiaDetailView(LoginRequiredMixin, DetailView):
    model=Noticia
    template_name='noticia/detalhar.html'
    context_object_name='noticia'


class NoticiaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model=Noticia
    template_name='noticia/cadastrar.html'
    form_class=NoticiaForm
    permission_required = 'noticia.pode_publicar'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia cadastrada com sucesso!")
        return reverse('listar-noticia')
    

class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model=Noticia
    template_name='noticia/atualizar.html'
    form_class=NoticiaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia atualizada com sucesso!")
        return reverse('listar-noticia')
    

class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model=Noticia
    template_name='noticia/noticia_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia deletada com sucesso!")
        return reverse('listar-noticia')
    

class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')