from django.shortcuts import render, redirect 
from django.urls import reverse
from .models import Autor
from .forms import AutorForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView


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

# def cadastrar(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Autor cadastradado com sucesso")
#             return redirect("cadastrar")
#     else:
#          form = AutorForm()
#          return render(request, 'cadastrar.html', {'form': form})
    
def atualizar(request, id):
    autor = Autor.objects.get(id=id)
    form = AutorForm(instance=autor)
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Autor atualizado com sucesso")
            return redirect("atualizar", id=id)
        else:
            return render(request, 'atualizar.html', {'form': form})
    else:
         return render(request, 'atualizar.html', {'form': form})

def deletar(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    messages.add_message(request, messages.WARNING, "Autor deletado")
    return redirect('listar')