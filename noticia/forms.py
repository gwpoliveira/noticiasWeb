from django.forms import ModelForm, EmailField, CharField
from .models import Autor, Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AutorForm(ModelForm):
   
    class Meta:
        model=Autor
        fields='__all__'

class NoticiaForm(ModelForm):
   
    class Meta:
        model=Noticia
        fields='__all__'

class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome:")
    lest_name = CharField(max_length=150, label="Sobrenome:")
    email = EmailField(max_length=150, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name','lest_name','email', 'password1', 'password2' ]
        