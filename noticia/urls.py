from django.contrib import admin
from django.urls import path
from .views import AutoDetailView, AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView


urlpatterns = [
    path('', AutorListView.as_view(), name='listar'),
    path('<int:id>', AutoDetailView.as_view(), name='detalhar'),
    path('cadastrar/', AutorCreateView.as_view(), name='cadastrar'),
    path('atualizar/<int:id>', AutorUpdateView.as_view(), name='atualizar'),
    path('deletar/<int:id>', AutorDeleteView.as_view(), name='deletar')
]