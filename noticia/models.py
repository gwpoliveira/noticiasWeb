from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome_Categoria = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    def __str__(self):        
        return f'{self.nome_Categoria}'

class Autor(models.Model):
    nome_Autor = models.CharField(max_length=200)
    data_Nascimento = models.DateField(default='1978-01-01')
    email=models.EmailField()
    idade=models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    def __str__(self):        
        return f'{self.nome_Autor}'