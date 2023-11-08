from django.contrib import admin
from django.urls import path
from .views import AutoDetailView, AutorListView, AutorCreateView, atualizar, deletar


urlpatterns = [
    path('', AutorListView.as_view(), name='listar'),
    path('<int:id>', AutoDetailView.as_view(), name='detalhar'),
    path('cadastrar/', AutorCreateView.as_view(), name='cadastrar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('deletar/<int:id>', deletar, name='deletar')
]