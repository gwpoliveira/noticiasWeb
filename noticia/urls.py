from django.urls import path
from .views import detalhar,listar, cadastrar



urlpatterns = [
    path('', listar, name='listar'),
    path('<int:id>',detalhar, name='detalhar'),
    path('cadastrar/', cadastrar, name='cadastrar')
]